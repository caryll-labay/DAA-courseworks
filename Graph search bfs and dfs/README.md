[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10457258&assignment_repo_type=AssignmentRepo)
# Graph Algorithms Challenge

In this coding challenge, you will be implementing two graph algorithms, Breadth-First Search (BFS) and Depth-First Search (DFS). You will be given an undirected graph represented as an adjacency list, and you need to write two functions, `bfs` and `dfs`, that traverse the graph starting from a given source node and return the nodes visited in the order they were visited.

## Function Signatures


```py

def bfs(graph: Dict[Union[int, str], List[Union[int, str]]], source: Union[int, str]) -> List[Union[int, str]]:
    pass


def dfs(graph: Dict[Union[int, str], List[Union[int, str]]], source: Union[int, str]) -> List[Union[int, str]]:
    pass

```

## Input

The input to the functions are:

- `graph`: A dictionary that represents the graph. The keys of the dictionary are integers or string representing the nodes, and the values are lists of integers representing the nodes adjacent to the key node. For example, the following dictionary represents a graph with nodes 1, 2, and 3, where node 1 is adjacent to nodes 2 and 3, and node 2 is adjacent to node 3:
```py
{
    1: [2, 3],
    2: [3],
    3: []
}
```

- `source`: An integer representing the source node to start the traversal from.



## Output

The output of the functions should be a list of integers representing the nodes visited in the order they were visited.


## Constraints

- The input graph will have at most 10^5 nodes and 10^5 edges.
- The input graph will be connected.
- The input graph may contain self-loops and parallel edges.

## Testing

You may run the basic test using the command `python test.py` to check if your code works
