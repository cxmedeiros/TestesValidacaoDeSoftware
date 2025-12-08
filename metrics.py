import ast
import subprocess
import re
import json
import inspect
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class FunctionMetrics:
    """Métricas de uma função individual."""
    name: str
    cyclomatic_complexity: int = 0
    line_start: int = 0
    line_end: int = 0
    total_lines: int = 0
    lines_covered: int = 0
    tests_generated: int = 0
    tests_valid_syntax: int = 0
    tests_passed: int = 0
    tests_failed: int = 0
    coverage_percent: float = 0.0


@dataclass
class TestRunMetrics:
    """Métricas de uma execução completa."""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    total_functions: int = 0
    total_tests_generated: int = 0
    total_tests_valid: int = 0
    total_tests_passed: int = 0
    total_tests_failed: int = 0
    overall_coverage: float = 0.0
    syntax_success_rate: float = 0.0
    test_pass_rate: float = 0.0
    functions: list = field(default_factory=list)


def calculate_cyclomatic_complexity(func_source: str) -> int:
    """Calcula a complexidade ciclomática de uma função."""
    try:
        tree = ast.parse(func_source)
    except SyntaxError:
        return 0
    
    complexity = 1
    
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.While, ast.For)):
            complexity += 1
        elif isinstance(node, ast.BoolOp):
            complexity += len(node.values) - 1
        elif isinstance(node, ast.ExceptHandler):
            complexity += 1
        elif isinstance(node, ast.Match):
            complexity += len(node.cases) - 1
        elif isinstance(node, ast.comprehension):
            complexity += len(node.ifs)
    
    return complexity


def get_function_lines(func_obj) -> tuple[int, int]:
    """Retorna as linhas de início e fim de uma função."""
    try:
        source_lines, start_line = inspect.getsourcelines(func_obj)
        end_line = start_line + len(source_lines) - 1
        return start_line, end_line
    except Exception:
        return 0, 0


def validate_syntax(code: str) -> tuple[bool, Optional[str]]:
    """Verifica se o código tem sintaxe Python válida."""
    try:
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, str(e)


def count_test_functions(code: str) -> int:
    """Conta quantas funções de teste existem no código."""
    try:
        tree = ast.parse(code)
        count = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
                count += 1
        return count
    except SyntaxError:
        return 0


def run_all_tests_with_coverage(tests_dir: Path) -> dict:
    """
    Executa TODOS os testes de uma vez e retorna dados de cobertura detalhados.
    """
    # Limpa arquivos de cobertura anteriores
    for f in [Path("coverage.json"), Path(".coverage")]:
        f.unlink(missing_ok=True)
    
    command = [
        "pytest",
        str(tests_dir),
        "--cov=dataset.funcoes_ramificadas",
        "--cov-report=json:coverage.json",
        "-v",
        "--tb=no"
    ]
    
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=300
        )
        
        output = result.stdout + result.stderr
        
        # Debug: mostrar parte da saída
        print(f"   Saída pytest (primeiros 500 chars):")
        print(f"   {output[:500]}")
        
        # Parse resultados por arquivo de teste
        test_results = {}
        
        # Múltiplos padrões de regex para capturar resultados
        # Padrão 1: tests/test_average.py::test_average_lista_vazia PASSED
        # Padrão 2: test_average.py::test_average_lista_vazia PASSED
        # Padrão 3: PASSED tests/test_average.py::test_func
        patterns = [
            r'test_(\w+)\.py::(\w+)\s+(PASSED|FAILED)',
            r'(PASSED|FAILED)\s+test_(\w+)\.py::(\w+)',
        ]
        
        for pattern in patterns:
            for match in re.finditer(pattern, output):
                groups = match.groups()
                
                # Identifica qual grupo é o nome da função e qual é o status
                if groups[0] in ('PASSED', 'FAILED'):
                    status = groups[0]
                    func_name = groups[1]
                else:
                    func_name = groups[0]
                    status = groups[2] if len(groups) > 2 else groups[1]
                
                if func_name not in test_results:
                    test_results[func_name] = {"passed": 0, "failed": 0}
                
                if status == "PASSED":
                    test_results[func_name]["passed"] += 1
                else:
                    test_results[func_name]["failed"] += 1
        
        # Também tenta pegar do resumo final
        # Formato: "X passed, Y failed" ou "X passed"
        summary_passed = re.search(r'(\d+)\s+passed', output)
        summary_failed = re.search(r'(\d+)\s+failed', output)
        
        total_passed = int(summary_passed.group(1)) if summary_passed else 0
        total_failed = int(summary_failed.group(1)) if summary_failed else 0
        
        print(f"   Total do resumo: {total_passed} passed, {total_failed} failed")
        print(f"   Funções detectadas: {list(test_results.keys())[:5]}...")
        
        # Lê dados de cobertura
        coverage_data = {}
        cov_file = Path("coverage.json")
        
        if cov_file.exists():
            print(f"   ✅ coverage.json encontrado")
            try:
                with open(cov_file) as f:
                    cov_json = json.load(f)
                    
                    # Debug: mostrar estrutura
                    print(f"   Arquivos no coverage: {list(cov_json.get('files', {}).keys())[:3]}...")
                    
                    # Procura pelo arquivo de funções
                    for file_path, file_data in cov_json.get("files", {}).items():
                        if "funcoes_ramificadas" in file_path:
                            print(f"   Encontrado: {file_path}")
                            coverage_data = {
                                "executed_lines": set(file_data.get("executed_lines", [])),
                                "missing_lines": set(file_data.get("missing_lines", [])),
                            }
                            print(f"   Linhas executadas: {len(coverage_data['executed_lines'])}")
                            print(f"   Linhas faltando: {len(coverage_data['missing_lines'])}")
                            break
            except Exception as e:
                print(f"   ❌ Erro ao ler coverage.json: {e}")
        else:
            print(f"   ❌ coverage.json NÃO encontrado")
        
        # Se não conseguiu detectar por regex, distribui proporcionalmente
        if not test_results and total_passed > 0:
            print("   ⚠️ Usando fallback para distribuir resultados")
        
        return {
            "test_results": test_results,
            "coverage_data": coverage_data,
            "summary": {"passed": total_passed, "failed": total_failed}
        }
        
    except subprocess.TimeoutExpired:
        print("❌ Timeout ao executar testes")
        return {"test_results": {}, "coverage_data": {}, "summary": {}}
    except Exception as e:
        print(f"❌ Erro ao executar testes: {e}")
        return {"test_results": {}, "coverage_data": {}, "summary": {}}


def calculate_function_coverage(
    line_start: int, 
    line_end: int, 
    executed_lines: set, 
    missing_lines: set
) -> tuple[int, int, float]:
    """
    Calcula cobertura para uma função específica baseado em suas linhas.
    """
    func_lines = set(range(line_start, line_end + 1))
    
    covered = func_lines & executed_lines
    not_covered = func_lines & missing_lines
    
    total_executable = len(covered) + len(not_covered)
    
    if total_executable == 0:
        return 0, 0, 0.0
    
    coverage_percent = (len(covered) / total_executable) * 100
    return total_executable, len(covered), coverage_percent


def analyze_test_file_syntax(test_file: Path) -> tuple[bool, int]:
    """Analisa sintaxe e conta testes de um arquivo."""
    if not test_file.exists():
        return False, 0
    
    code = test_file.read_text(encoding='utf-8')
    is_valid, _ = validate_syntax(code)
    
    if is_valid:
        return True, count_test_functions(code)
    return False, 0


def generate_report(metrics: TestRunMetrics) -> str:
    """Gera relatório formatado das métricas."""
    report = []
    report.append("=" * 70)
    report.append("📊 RELATÓRIO DE MÉTRICAS - GERAÇÃO DE TESTES")
    report.append("=" * 70)
    report.append(f"📅 Timestamp: {metrics.timestamp}")
    report.append("")
    
    report.append("📈 RESUMO GERAL")
    report.append("-" * 50)
    report.append(f"  Funções analisadas:     {metrics.total_functions}")
    report.append(f"  Testes gerados:         {metrics.total_tests_generated}")
    report.append(f"  Testes válidos:         {metrics.total_tests_valid}")
    report.append(f"  Testes passando:        {metrics.total_tests_passed}")
    report.append(f"  Testes falhando:        {metrics.total_tests_failed}")
    report.append("")
    
    report.append("📊 TAXAS")
    report.append("-" * 50)
    report.append(f"  Taxa de sintaxe válida: {metrics.syntax_success_rate:.1f}%")
    report.append(f"  Taxa de testes OK:      {metrics.test_pass_rate:.1f}%")
    report.append(f"  Cobertura média:        {metrics.overall_coverage:.1f}%")
    report.append("")
    
    report.append("📋 DETALHES POR FUNÇÃO (ordenado por cobertura)")
    report.append("-" * 50)
    
    sorted_funcs = sorted(metrics.functions, key=lambda x: x.coverage_percent)
    
    for func in sorted_funcs:
        if func.tests_generated == 0:
            status = "⚪"
        elif func.tests_failed > 0:
            status = "❌"
        elif func.coverage_percent >= 80:
            status = "✅"
        elif func.coverage_percent >= 50:
            status = "🟡"
        else:
            status = "🟠"
        
        report.append(f"  {status} {func.name}")
        report.append(f"      CC: {func.cyclomatic_complexity:2d} | "
                     f"Testes: {func.tests_generated:2d} | "
                     f"Pass: {func.tests_passed:2d} | "
                     f"Fail: {func.tests_failed:2d} | "
                     f"Cov: {func.coverage_percent:5.1f}%")
    
    report.append("")
    report.append("Legenda: ✅ ≥80% | 🟡 ≥50% | 🟠 <50% | ❌ Falhas | ⚪ Sem testes")
    report.append("=" * 70)
    
    return "\n".join(report)


def save_metrics_json(metrics: TestRunMetrics, output_file: Path):
    """Salva métricas em formato JSON para análise posterior."""
    data = {
        "timestamp": metrics.timestamp,
        "summary": {
            "total_functions": metrics.total_functions,
            "total_tests_generated": metrics.total_tests_generated,
            "total_tests_valid": metrics.total_tests_valid,
            "total_tests_passed": metrics.total_tests_passed,
            "total_tests_failed": metrics.total_tests_failed,
            "syntax_success_rate": round(metrics.syntax_success_rate, 2),
            "test_pass_rate": round(metrics.test_pass_rate, 2),
            "overall_coverage": round(metrics.overall_coverage, 2),
        },
        "functions": [
            {
                "name": f.name,
                "cyclomatic_complexity": f.cyclomatic_complexity,
                "line_start": f.line_start,
                "line_end": f.line_end,
                "total_lines": f.total_lines,
                "lines_covered": f.lines_covered,
                "tests_generated": f.tests_generated,
                "tests_valid_syntax": f.tests_valid_syntax,
                "tests_passed": f.tests_passed,
                "tests_failed": f.tests_failed,
                "coverage_percent": round(f.coverage_percent, 2),
            }
            for f in metrics.functions
        ]
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def run_full_analysis(tests_dir: Path = Path("tests")) -> TestRunMetrics:
    """Executa análise completa de todos os testes gerados."""
    import dataset.funcoes_ramificadas as funcs_module
    
    metrics = TestRunMetrics()
    
    print("📂 Coletando informações das funções...")
    
    functions_info = []
    for name, obj in inspect.getmembers(funcs_module):
        if inspect.isfunction(obj):
            line_start, line_end = get_function_lines(obj)
            try:
                source = inspect.getsource(obj)
                cc = calculate_cyclomatic_complexity(source)
            except Exception:
                cc = 0
            
            functions_info.append({
                "name": name,
                "obj": obj,
                "line_start": line_start,
                "line_end": line_end,
                "cyclomatic_complexity": cc
            })
    
    metrics.total_functions = len(functions_info)
    print(f"   Encontradas {metrics.total_functions} funções")
    
    print("\n🧪 Executando todos os testes...")
    all_results = run_all_tests_with_coverage(tests_dir)
    test_results = all_results.get("test_results", {})
    coverage_data = all_results.get("coverage_data", {})
    summary = all_results.get("summary", {})
    
    executed_lines = coverage_data.get("executed_lines", set())
    missing_lines = coverage_data.get("missing_lines", set())
    
    print("\n📊 Calculando métricas por função...")
    
    for func_info in functions_info:
        func_name = func_info["name"]
        test_file = tests_dir / f"test_{func_name}.py"
        
        func_metrics = FunctionMetrics(
            name=func_name,
            cyclomatic_complexity=func_info["cyclomatic_complexity"],
            line_start=func_info["line_start"],
            line_end=func_info["line_end"]
        )
        
        is_valid, test_count = analyze_test_file_syntax(test_file)
        func_metrics.tests_generated = test_count
        func_metrics.tests_valid_syntax = test_count if is_valid else 0
        
        if func_name in test_results:
            func_metrics.tests_passed = test_results[func_name]["passed"]
            func_metrics.tests_failed = test_results[func_name]["failed"]
        
        if executed_lines or missing_lines:
            total, covered, percent = calculate_function_coverage(
                func_info["line_start"],
                func_info["line_end"],
                executed_lines,
                missing_lines
            )
            func_metrics.total_lines = total
            func_metrics.lines_covered = covered
            func_metrics.coverage_percent = percent
        
        metrics.functions.append(func_metrics)
        metrics.total_tests_generated += func_metrics.tests_generated
        metrics.total_tests_valid += func_metrics.tests_valid_syntax
        metrics.total_tests_passed += func_metrics.tests_passed
        metrics.total_tests_failed += func_metrics.tests_failed
    
    # Se não conseguiu capturar individualmente, usa o resumo
    if metrics.total_tests_passed == 0 and summary.get("passed", 0) > 0:
        print("   ⚠️ Usando totais do resumo do pytest")
        metrics.total_tests_passed = summary.get("passed", 0)
        metrics.total_tests_failed = summary.get("failed", 0)
    
    if metrics.total_tests_generated > 0:
        metrics.syntax_success_rate = (metrics.total_tests_valid / metrics.total_tests_generated) * 100
    
    total_executed = metrics.total_tests_passed + metrics.total_tests_failed
    if total_executed > 0:
        metrics.test_pass_rate = (metrics.total_tests_passed / total_executed) * 100
    
    coverages = [f.coverage_percent for f in metrics.functions if f.tests_generated > 0]
    if coverages:
        metrics.overall_coverage = sum(coverages) / len(coverages)
    
    return metrics


if __name__ == "__main__":
    print("🔍 Analisando testes gerados...\n")
    
    metrics = run_full_analysis()
    
    print("\n")
    report = generate_report(metrics)
    print(report)
    
    output_file = Path("metrics_report.json")
    save_metrics_json(metrics, output_file)
    print(f"\n📁 Métricas salvas em: {output_file}")
