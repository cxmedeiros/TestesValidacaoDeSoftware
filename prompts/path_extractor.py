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

