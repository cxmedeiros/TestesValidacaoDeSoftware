import ast
import inspect
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import dataset.funcoes_ramificadas
from prompts import UNIT_TEST_PROMPT_TEMPLATE, PROMPT_PATH_EXTRACTOR
import subprocess
import re

from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()

def get_functions_from_module(module):
    functions = []
    for _, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            functions.append(obj)
    return functions

def extract_paths_with_llm(func, llm):
    """Extrai a AST da função, envia para a LLM para tradução em linguagem natural dos caminhos."""
    source = inspect.getsource(func)
    tree = ast.parse(source)
    ast_str = ast.dump(tree, indent=4)

    prompt_intermediate = PromptTemplate(
        input_variables=["ast_dump"],
        template= PROMPT_PATH_EXTRACTOR
    )
    prompt = prompt_intermediate.format(ast_dump=ast_str)

    response = llm([HumanMessage(content=prompt)]).content

    return response


def get_function_context(func):
    """Extrai contexto completo da função: assinatura, tipos e docstring"""
    sig = inspect.signature(func)
    signature_str = f"{func.__name__}{sig}"
    
    type_info = []
    for param_name, param in sig.parameters.items():
        if param.annotation != inspect.Parameter.empty:
            type_info.append(f"{param_name}: {param.annotation}")
        else:
            type_info.append(f"{param_name}: Any")
    
    docstring = func.__doc__ or "Sem documentação disponível"
    
    return_type = sig.return_annotation
    if return_type == inspect.Signature.empty:
        return_type_str = "Any"
    else:
        return_type_str = str(return_type)
    
    return {
        "signature": signature_str,
        "parameters": ", ".join(type_info),
        "docstring": docstring.strip(),
        "return_type": return_type_str
    }

def run_tests_and_get_coverage(test_file, module_to_cover):

    print(f"\nExecutando testes em: {test_file}")

    command = [
        "pytest", 
        test_file, 
        f"--cov={module_to_cover.__name__}", 
        "--cov-report=term-missing", 
        "-s",
        "-v"
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
        
        match = re.search(r"TOTAL\s+\d+\s+\d+\s+(\d+)%", result.stdout)
        if match:
            coverage_percentage = int(match.group(1))
            return coverage_percentage
        
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar pytest para {test_file}:")
        print(e.stdout)
        print(e.stderr)
    
    return 0

def get_test_function_template(function_name, test):

    return (
    "import sys\n"
    "import os\n"
    "sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\n"
    f"from dataset.funcoes_ramificadas import {function_name}\n\n"
    + test
    )

def write_test_file(function_name, tests):
    """Escreve os testes em um arquivo seguindo padrão pytest/unittest"""
    
    test_filename = f"tests/test_{function_name}.py"

    test_content = ""

    for i, test in enumerate(tests):
        test_content += get_test_function_template(function_name, test)

    with open(test_filename, 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    print(f"Arquivo de teste criado: {test_filename}")
    
    return test_filename

def generate_tests_with_langchain(func, llm, prompt, paths_description):
    function_name = func.__name__
    context = get_function_context(func)
    tests = []

    formatted_prompt = prompt.format(
        function_name=function_name,
        path_description=paths_description,
        signature=context["signature"],
        parameters=context["parameters"],
        docstring=context["docstring"],
        return_type=context["return_type"]
    )

    raw_result = llm([HumanMessage(content=formatted_prompt)]).content
    tests.append(raw_result)

    return tests


if __name__ == "__main__":
    
    llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0)

    prompt = PromptTemplate(
        input_variables=["function_name", "path_description", "signature", "parameters", "docstring", "return_type"],
        template=UNIT_TEST_PROMPT_TEMPLATE
    )

    for function in get_functions_from_module(dataset.funcoes_ramificadas):
        paths_description = extract_paths_with_llm(function, llm)

        tests = generate_tests_with_langchain(function, llm, prompt, paths_description)

        test_file = write_test_file(function.__name__, tests)

    coverage = run_tests_and_get_coverage('./tests', dataset.funcoes_ramificadas)

    print(f"\nProcesso concluído!")
    print(f"Para executar todos os testes gerados: pytest test_*.py")

