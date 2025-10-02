# Autores: Lucca, Diego, Joud
# main.py - Executa exemplos de rotas

from metro import menor_tempo_dp

def exemplo():
    origem, destino, hora = "Kings Cross", "Victoria", "10:30"
    for modo in ["menor", "medio", "maior"]:
        print(f"\n--- Rota {modo.upper()} ---")
        res = menor_tempo_dp(origem, destino, hora, modo)
        if not res:
            print("Nenhum caminho encontrado."); continue
        print("Tempo total:", res["tempo_total_min"], "min")
        print("Caminho:", " -> ".join(res["caminho"]))
        print("Linhas:", " -> ".join(res["linhas"]))
        print("Trocas de linha:", res["trocas"])

if __name__ == "__main__":
    exemplo()
