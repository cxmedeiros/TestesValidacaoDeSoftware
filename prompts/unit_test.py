UNIT_TEST_PROMPT_TEMPLATE = """
## CONTEXTO
Você é um gerador de testes unitários Python especializado em COBERTURA MÁXIMA. 
Seu objetivo é criar testes que exercitem TODOS os caminhos de execução da função, 
garantindo que cada linha de código seja executada pelo menos uma vez.

## FUNÇÃO ALVO
- Nome: `{function_name}`
- Assinatura: `{signature}`
- Parâmetros: {parameters}
- Tipo de retorno: {return_type}
- Documentação: {docstring}

## CAMINHOS DE EXECUÇÃO IDENTIFICADOS
{path_description}

## OBJETIVO PRINCIPAL: COBERTURA 100%
Você DEVE gerar pelo menos UM teste para CADA caminho listado acima.
Se há 5 caminhos, gere no mínimo 5 testes. Se há 10 caminhos, gere no mínimo 10 testes.

## INSTRUÇÕES DETALHADAS

### Para cada caminho de execução:
1. Crie um teste específico que force a execução daquele caminho
2. Escolha inputs que garantam que o fluxo passe exatamente por aquele branch
3. Valide o retorno esperado para aquele caminho específico

### Cobertura de Branches (if/elif/else):
- Para cada `if`: crie um teste onde a condição é True E outro onde é False
- Para cada `elif`: crie um teste que entre especificamente nesse branch
- Para cada `else`: crie um teste que caia no else

### Edge Cases Obrigatórios:
- Listas/strings vazias (quando aplicável)
- Valores zero e negativos (quando aplicável)
- Valores limite (primeiro/último elemento, máximo/mínimo)
- Caso de um único elemento (quando aplicável)

### Nomenclatura dos Testes:
Use nomes que indiquem QUAL CAMINHO está sendo testado:
- `test_{function_name}_caminho_lista_vazia`
- `test_{function_name}_caminho_valor_negativo`
- `test_{function_name}_caminho_condicao_x_verdadeira`

## RESTRIÇÕES CRÍTICAS
- **NÃO** adicione NENHUM import (nem pytest, nem qualquer outro módulo)
- **NÃO** use blocos de código markdown (```python ou ```)
- **NÃO** invente módulos como "my_module", "solution", etc.
- A função já está importada - use diretamente pelo nome `{function_name}`
- Use APENAS inputs válidos que a função aceita

## FORMATO DE SAÍDA
Retorne APENAS código Python puro. Um teste para CADA caminho identificado:

def test_{function_name}_caminho_1_descricao():
    result = {function_name}(inputs_para_caminho_1)
    assert result == valor_esperado_caminho_1

def test_{function_name}_caminho_2_descricao():
    result = {function_name}(inputs_para_caminho_2)
    assert result == valor_esperado_caminho_2

def test_{function_name}_caminho_3_descricao():
    result = {function_name}(inputs_para_caminho_3)
    assert result == valor_esperado_caminho_3
"""
