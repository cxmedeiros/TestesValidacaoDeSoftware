# Geração de Casos de Teste para Caminhos de Execução Específicos em um Módulo Pequeno

**Projeto da disciplina Tópicos Avançados em Engenharia de Software (TAES)**  
**Centro de Informática – Universidade Federal de Pernambuco (UFPE)**

---

## 📘 Descrição

Este projeto investiga o uso de *Large Language Models (LLMs)* na geração automática de casos de teste para caminhos de execução específicos em funções Python. A proposta é inspirada na técnica **Path Constraint Prompting**, introduzida no artigo *SymPrompt*.

---

## 🎯 Objetivo

Implementar um protótipo que, a partir de uma função Python:

- Identifique seus caminhos de execução (ex.: estruturas `if/else`);
- Formule prompts específicos que orientem o LLM a gerar testes;
- Verifique se os testes gerados cobrem corretamente os caminhos especificados.

---

## ⚙️ Metodologia

1. **Seleção da função**  
   Escolher uma função Python com 2 a 4 caminhos de execução distintos.

2. **Análise estática simplificada**  
   Utilizar uma abordagem manual ou uma biblioteca como `ast` para identificar as ramificações da função.

3. **Formulação dos prompts**  
   Criar prompts contendo:
   - O código da função;
   - A descrição do caminho de execução desejado.

4. **Geração e verificação dos testes**  
   - Utilizar um LLM (como `gpt-3.5-turbo` ou um modelo local) para gerar os testes;
   - Verificar manualmente ou com ferramentas como `coverage.py` se os testes cobrem os caminhos esperados.

---

## 🧠 Fundamentação

Este projeto reproduz dois elementos centrais do artigo *SymPrompt*:

- O conceito de **Path Constraint Prompting**;
- A abordagem de decomposição em múltiplas etapas para a geração de casos de teste com LLMs.

---

## 👥 Integrantes

| Nome completo                   | Login institucional |
|---------------------------------|----------------------|
| Kailane Eduarda Felix da Silva  | kefs                 |
| Maria Vitória Soares Muniz      | mvsm3                |
| Camila Xavier Medeiros          | cxm                  |
| Gabriel Lopes de Souza          | gls6                 |


