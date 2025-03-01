
from solution import bfs, dfs

# Define a simple graph
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# Test BFS function
bfs_result = bfs(graph, 2)
assert bfs_result == [2, 0, 3, 1], f"Failed for graph {graph} and source 2"

# Test DFS function
dfs_result = dfs(graph, 2)
assert dfs_result == [2, 0, 1, 3], f"Failed for graph {graph} and source 2"

print("All tests passed")



##############################################
## do not edit this part

def decode_base64(encoded_string):
    import base64
    import json
    return json.loads(base64.b64decode(encoded_string).decode('utf-8'))

import sys
if "-score" in sys.argv:
  graph = decode_base64(sys.argv[-2])
  start = sys.argv[-1]
  print(bfs(graph, start))
  print(dfs(graph, start))
