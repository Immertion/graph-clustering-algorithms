from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, vertex, visited, stack):
        visited[vertex] = True
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(vertex)

    def get_transpose(self):
        transposed_graph = Graph(self.vertices)
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                transposed_graph.add_edge(neighbor, vertex)
        return transposed_graph

    def kosaraju(self):
        stack = []
        visited = [False] * self.vertices

        for vertex in range(self.vertices):
            if not visited[vertex]:
                self.dfs(vertex, visited, stack)

        transposed_graph = self.get_transpose()

        visited = [False] * self.vertices
        strongly_connected_components = []

        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                current_component = []
                transposed_graph.dfs(vertex, visited, current_component)
                strongly_connected_components.append(current_component)

        return strongly_connected_components

# Пример использования
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

print("Компоненты сильной связности:")
print(g.kosaraju())