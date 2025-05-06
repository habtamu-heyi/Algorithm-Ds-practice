# ----------- GRAPH ALGORITHMS -----------
from collections import deque

def bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    visited = set()
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend(graph[node])
    return order