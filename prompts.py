UNIT_TEST_PROMPT_TEMPLATE = """
## CONTEXTO
Você é um gerador de testes unitários Python usando pytest. Seu objetivo é criar testes completos, claros e robustos para uma 
função específica com base na assinatura, parâmetros, tipo de retorno, docstring e uma lista de caminhos de execução fornecidos.

## FUNÇÃO ALVO
- Nome: `{function_name}`
- Assinatura: `{signature}`
- Parâmetros: {parameters}
- Tipo de retorno: {return_type}
- Documentação: {docstring}

## CAMINHOS DE EXECUÇÃO
{path_description}

## INSTRUÇÕES
Escreva um caso de teste em Python utilizando pytest para cada caminho descrito. Garanta que:

1. **Nome da função de teste seja descritivo** - Indique claramente o caminho/cenário testado
2. **Valores de entrada adequados** - Escolha inputs que percorram exatamente o caminho descrito
3. **Assertions completas** - Valide o resultado esperado e possíveis efeitos colaterais
4. **Teste robusto e preciso** - Cubra o caminho de forma completa

## DIRETRIZES
- Analise cuidadosamente assinatura, parâmetros e docstring para entender o comportamento
- Infira o resultado esperado com base no tipo de retorno e caminho específico
- Use valores razoáveis para parâmetros sem tipo explícito
- Gere um teste funcional e completo para cada caminho
- Evite código redundante ou desnecessário

## RESTRIÇÕES
- Não adicione imports desnecessários

## FORMATO DE SAÍDA
Retorne APENAS o código dos testes, sem explicações adicionais:

def test_nome_descritivo_caminho_1():
    result = function_name(parametros)
    assert result == valor_esperado

def test_nome_descritivo_caminho_2():
    result = function_name(outros_parametros)
    assert result == outro_resultado
"""

PROMPT_PATH_EXTRACTOR = """
Analise a AST da função Python abaixo e identifique todos os caminhos de execução que terminam em `return`.

## AST DA FUNÇÃO
{ast_dump}

## INSTRUÇÕES
- Considere apenas fluxos que levam diretamente a um `return`
- Ignore caminhos incompletos ou que não terminam em `return`
- Analise todas as estruturas de controle: `if/else/elif`, loops, tratamento de exceções
- Descreva cada caminho de forma clara e sequencial

## FORMATO DE RESPOSTA
Retorne apenas uma lista numerada com as descrições dos caminhos:

1. [Descrição clara do primeiro caminho até return]
2. [Descrição clara do segundo caminho até return]
...

## EXEMPLO
Para a função:
```python
def max_in_list(lst):
    if not lst:
        return None
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val
```

Resposta esperada:
1. Se a lista estiver vazia, retorna None imediatamente
2. Se a lista não estiver vazia, percorre todos os elementos e retorna o maior valor encontrado

Não adicione explicações extras. Retorne APENAS a lista numerada dos caminhos.
"""
