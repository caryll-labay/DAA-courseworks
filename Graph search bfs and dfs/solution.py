from typing import Dict, List, Union
from collections import deque


def bfs(graph: Dict[Union[int, str], List[Union[int, str]]], source: Union[int, str]) -> List[Union[int, str]]:
    visited = set()
    queue = deque([source])
    path = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            path.append(node)
            queue.extend(graph[node])
    return path

def dfs(graph: Dict[Union[int, str], List[Union[int, str]]], source: Union[int, str]) -> List[Union[int, str]]:
    visited = set()
    path = []
    def dfs_helper(node):
        visited.add(node)
        path.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)
    dfs_helper(source)
    return path
