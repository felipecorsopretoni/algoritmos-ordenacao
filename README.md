# Análise Experimental de Algoritmos de Ordenação

Implementação e comparação experimental de três algoritmos de ordenação desenvolvida para a disciplina de Fundamentos da Teoria da Computação e Análise de Algoritmos — PUC-Campinas.

## Algoritmos implementados

| Algoritmo | Complexidade (caso médio) | Complexidade (pior caso) |
|---|---|---|
| Insertion Sort | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n²) |

## Metodologia

- Vetores gerados aleatoriamente com seed fixo (42) para garantir comparação justa
- Tamanhos testados: 1.000, 10.000 e 100.000 elementos
- 3 execuções por algoritmo/tamanho
- Métricas coletadas: tempo de execução (s), tempo médio, desvio padrão e quantidade de trocas/movimentações

## Resultados

| Algoritmo | n=1.000 | n=10.000 | n=100.000 |
|---|---|---|---|
| Insertion Sort | 0,022s | 2,090s | N/C (>5 min) |
| Merge Sort | 0,004s | 0,024s | 0,305s |
| Quick Sort | 0,003s | 0,016s | 0,199s |

## Como executar

```bash
python insertion_sort.py
python merge_sort.py
python quick_sort.py
```

## Ambiente

- Linguagem: Python 3.12
- Sistema operacional: Windows 11
- Processador: Intel Core i5-1235U (12ª geração)
- Memória RAM: 16 GB
