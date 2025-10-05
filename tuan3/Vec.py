import math
def cosineb2v(u, v):
    dot = sum(a * b for a, b in zip(u, v))
    norm_u = math.sqrt(sum(c ** 2 for c in u))
    norm_v = math.sqrt(sum(c ** 2 for c in v))
    if norm_u == 0 or norm_v == 0:  # tránh chia cho 0
        return 0
    return dot / (norm_u * norm_v)