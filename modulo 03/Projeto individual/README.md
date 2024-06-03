# Projeto Individual - Análise de Desempenho de Desenvolvedores

## Introdução
Este projeto tem como objetivo analisar o desempenho de desenvolvedores ao longo de uma semana, utilizando dados sobre horas trabalhadas, bugs corrigidos e tarefas concluídas. A análise inclui o cálculo de totais e médias para cada métrica, além da determinação da produtividade diária.

## Estrutura dos Dados
Os dados estão organizados em um arquivo Excel com as seguintes colunas:

- **Dia**: Dia da semana
- **Horas Trabalhadas**: Total de horas trabalhadas no dia
- **Bugs Corrigidos**: Número de bugs corrigidos no dia
- **Tarefas Concluídas**: Número de tarefas concluídas no dia

### Exemplo de Estrutura de Dados

| Dia      | Horas Trabalhadas | Bugs Corrigidos | Tarefas Concluidas |
|----------|-------------------|-----------------|--------------------|
| Segunda  | 6                 | 3               | 5                  |
| Terça    | 7                 | 2               | 4                  |
| Quarta   | 8                 | 1               | 6                  |
| Quinta   | 6                 | 4               | 4                  |
| Sexta    | 7                 | 3               | 5                  |
| Sábado   | 5                 | 2               | 3                  |
| Domingo  | 4                 | 1               | 2                  |

## Análises Realizadas

### Total e Média de Horas Trabalhadas
- **Total de Horas Trabalhadas**: 43
- **Média de Horas Trabalhadas por Dia**: 6.14

### Total e Média de Bugs Corrigidos
- **Total de Bugs Corrigidos**: 16
- **Média de Bugs Corrigidos por Dia**: 2.29

### Total e Média de Tarefas Concluídas
- **Total de Tarefas Concluídas**: 29
- **Média de Tarefas Concluídas por Dia**: 4.14

### Produtividade Diária (Tarefas Concluídas por Hora)
A produtividade diária foi calculada dividindo o número de tarefas concluídas pelo número de horas trabalhadas em cada dia.

- **Produtividade no Dia 1**: 0.83 tarefas/hora
- **Produtividade no Dia 2**: 0.57 tarefas/hora
- **Produtividade no Dia 3**: 0.75 tarefas/hora
- **Produtividade no Dia 4**: 0.67 tarefas/hora
- **Produtividade no Dia 5**: 0.71 tarefas/hora
- **Produtividade no Dia 6**: 0.60 tarefas/hora
- **Produtividade no Dia 7**: 0.50 tarefas/hora

## Conclusão
Este projeto forneceu uma visão detalhada sobre o desempenho dos desenvolvedores ao longo de uma semana. As métricas calculadas ajudam a entender a distribuição do trabalho, a eficiência na correção de bugs e a produtividade geral. Essas informações são valiosas para otimizar a alocação de recursos e melhorar a eficiência das equipes de desenvolvimento.

## Como Executar o Projeto

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```

2. **Instale as dependências necessárias:**
    ```bash
    pip install pandas
    ```

3. **Execute o script de análise:**
    ```python
    python analise_desenvolvedores.py
    ```
