from collections import deque


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": [],
    "D": [],
    "E": []
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for nei in graph[node]:
            dfs(nei)


def dfs_iter(start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for nei in reversed(graph[node]):
                stack.append(nei)

dfs("A")
print("\n --------")
dfs_iter("A")
print("\n --------")

# ----------------------
# BFS Starts From Here
# ----------------------

def bfs(start):
    visited = set()
    q = deque([start])

    visited.add(start)

    while q:
        node = q.popleft()
        print(node, end=" ")

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)

print("BFS: ", end=" ")
bfs("A")


count = 0
visited = set()
for node in graph:
    if node not in visited:
        dfs(node)
        count+=1

print("\nComponents = ", count)