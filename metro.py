# Autor: Lucca
# metro.py - Funções de cálculo: haversine, tempo, recursão + memoization

import math
from data import stations, edges

TRAIN_SPEED_KMH = 35.0
LINE_CHANGE_PENALTY_MIN = 4.0

# Distância geográfica (km)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*(math.sin(dlambda/2)**2)
    return R * (2 * math.atan2(math.sqrt(a), math.sqrt(1-a)))

# Tempo de viagem (minutos)
def travel_time_minutes(distance_km):
    return (distance_km / TRAIN_SPEED_KMH) * 60.0

# Tempo de espera por hora
def wait_time_minutes(current_minutes):
    hour = (current_minutes // 60) % 24
    if hour < 11:
        return 1.5
    elif hour >= 18:
        return 2.0
    return 1.0

# Monta grafo
def build_adjacency():
    adjacency = {s: [] for s in stations}
    for a, b, line in edges:
        d = haversine(*stations[a], *stations[b])
        adjacency[a].append((b, line, d))
        adjacency[b].append((a, line, d))
    return adjacency

# Calcula tempo total de um caminho
def compute_total_time(path_edges, hora_inicio):
    hh, mm = map(int, hora_inicio.split(":"))
    current_minutes, total = hh*60+mm, 0
    last_line = None
    for (line, dist_km) in path_edges:
        w = wait_time_minutes(current_minutes)
        if last_line and line != last_line:
            w += LINE_CHANGE_PENALTY_MIN
        t = travel_time_minutes(dist_km)
        total += w + t
        current_minutes += w + t
        last_line = line
    return total

# Busca recursiva com memoization
def find_paths(adjacency, origem, destino, hora_inicio):
    memo = {}
    def dfs(current, last_line, visited, path_nodes, path_edges):
        key = (current, last_line, tuple(sorted(visited)))
        if key in memo:
            return [list(p) for p in memo[key]]
        results = []
        if current == destino:
            total = compute_total_time(path_edges, hora_inicio)
            results.append((path_nodes[:], path_edges[:], total))
            memo[key] = results
            return results
        for (nei, line, dist) in adjacency[current]:
            if nei in visited: continue
            visited.add(nei)
            path_nodes.append(nei)
            path_edges.append((line, dist))
            results.extend(dfs(nei, line, visited, path_nodes, path_edges))
            visited.remove(nei)
            path_nodes.pop(); path_edges.pop()
        memo[key] = results
        return results
    return dfs(origem, None, {origem}, [origem], [])

# Função principal
def menor_tempo_dp(origem, destino, hora_inicio, modo='menor'):
    adj = build_adjacency()
    paths = find_paths(adj, origem, destino, hora_inicio)
    if not paths: return None
    paths.sort(key=lambda x: x[2])
    if modo == 'menor': chosen = paths[0]
    elif modo == 'maior': chosen = paths[-1]
    elif modo == 'medio': chosen = paths[len(paths)//2]
    else: raise ValueError("Modo inválido")
    nodes, edges, total = chosen
    linhas = [l for (l, _) in edges]
    trocas = sum(linhas[i]!=linhas[i-1] for i in range(1,len(linhas)))
    return {
        "tempo_total_min": round(total,2),
        "caminho": nodes,
        "linhas": linhas,
        "trocas": trocas
    }
