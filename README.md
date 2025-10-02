# CP2 - Dynamic Programming (Enunciado 1: Metrô de Londres)

Autores:  
- Lucca RM: 560731 → metro.py  
- Diego RM: 556724 → data.py  
- Joud RM: 556482 → main.py  

## Estrutura
- `data.py` → estações (lat/lon) + conexões (linha)  
- `metro.py` → funções de cálculo: Haversine, tempo de espera, recursão com memoization  
- `main.py` → exemplo de execução das rotas  
- `README.md` → este resumo  

## Hipóteses
- Velocidade média: 35 km/h  
- Espera dinâmica:  
  - antes das 11h → 1.5 min  
  - 11h–18h → 1.0 min  
  - após 18h → 2.0 min  
- Penalidade por troca de linha: +4 min  

## Como rodar
```bash
python main.py
