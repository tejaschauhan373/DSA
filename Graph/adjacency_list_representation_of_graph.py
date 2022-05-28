from collections import deque


class Graph:
    # UnDirected & UnWeighted Graph
    def __init__(self, v: int):
        self.total_vertices = v
        self.vertices = {i: set() for i in range(v)}

    def add_edge(self, i: int, j: int, un_dir: bool = True):

        self.vertices[i].add(j)
        if un_dir:
            self.vertices[j].add(i)

    def print_adjacency_list(self):
        # Iterate over all the rows
        for vertex, adjacent in self.vertices.items():
            print(vertex, "->", end="")
            for neighbour in adjacent:
                print(neighbour, end=", ")
            print()

    def bfs(self, source, destination: int = -1):
        """
        Time Complexity = O(N+E); N = number of nodes, E = number of edges
        Space Complexity = O(N)
        """
        queue = deque()
        visited = [False] * self.total_vertices
        # Single Source Shortest Path (SSSP) algorithm for undirected graph
        distance = [0] * self.total_vertices
        parent = [-1] * self.total_vertices

        queue.append(source)
        visited[source] = True
        parent[source] = source
        distance[source] = 0

        while queue:
            f = queue[0]
            print(f)
            queue.popleft()
            for nbr in self.vertices[f]:
                if not visited[nbr]:
                    queue.append(nbr)

                    # parent and dist
                    parent[nbr] = f
                    distance[nbr] = distance[f] + 1
                    visited[nbr] = True

        # print the shortest distance
        for i in range(self.total_vertices):
            print("Shortest distance to ", i, "is", distance[i])

        # print the path from a source to any destination
        if destination != -1:
            temp = destination
            while temp != source:
                print(temp, "-- ", end="")
                temp = parent[temp]
            print(source)

    def dfs(self, source):
        print()
        self.dfs_helper(source, [0] * self.total_vertices)
        print()

    def dfs_helper(self, node, visited):
        visited[node] = True
        print(node, end=", ")

        for nbr in self.vertices[node]:
            if not visited[nbr]:
                self.dfs_helper(nbr, visited)
        return

    def cycle_detection_dfs(self, node, visited, parent) -> bool:
        visited[node] = True
        for nbr in self.vertices[node]:
            if not visited[nbr]:
                nbr_found_cycle = self.cycle_detection_dfs(nbr, visited, node)
                if nbr_found_cycle:
                    return True
            elif nbr != parent:
                # nbr is visited and its not the parent of current node in the current dfs call
                return True
        return False

    def contains_cycle(self):
        visited = [False] * self.total_vertices
        return self.cycle_detection_dfs(0, visited, -1)


class Node:
    def __init__(self, name):
        self.neighbours = []
        self.name = name
        self.parents = []


class StringGraph:

    def __init__(self, cities: list):
        self.vertices = {}
        for city in cities:
            self.vertices[city] = Node(city)

    def add_edge(self, vertex: str, neighbour: str, un_dir: bool = False):
        self.vertices[vertex].neighbours.append(neighbour)
        if un_dir:
            self.vertices[neighbour].neighbours.append(vertex)

    def print_adjacency_list(self):
        # Iterate over all the rows
        for vertex, adjacent in self.vertices.items():
            print(vertex, "->", end="")
            for neighbour in adjacent.neighbours:
                print(neighbour, end=", ")
            print()


class WeightedDirectedGraph:

    def __init__(self, nodes: list):
        self.vertices = {}
        for name in nodes:
            self.vertices[name] = Node(name)

    def add_edge(self, vertex, neighbour, weight, un_dir: bool = False):
        self.vertices[vertex].neighbours.append((neighbour, weight))
        if un_dir:
            self.vertices[neighbour].neighbours.append((vertex, weight))

    def print_adjacency_list(self):
        # Iterate over all the rows
        for vertex, adjacent in self.vertices.items():
            print(vertex, "->", end="")
            for neighbour in adjacent.neighbours:
                print(neighbour, end=", ")
            print()

    def dijkstra(self, source, dest):

        # Data Structures
        distance = [float("+inf")] * len(self.vertices)
        s = deque()
        # 1. Initialize
        distance[source] = 0
        s.append((0, source))  # (minimum distance, source node)
        while s:
            curr = s[0]

            node = curr[1]
            dist_till_now = curr[0]
            s.popleft()
            for nbr_pair in self.vertices[node].neighbours:
                nbr = nbr_pair[0]
                current_edge = nbr_pair[1]
                if dist_till_now + current_edge < distance[nbr]:
                    # remove if nbr already exist in the set
                    try:
                        s.remove((distance[nbr], nbr))
                    except ValueError:
                        pass
                    # insert updated value with new dist
                    distance[nbr] = dist_till_now + current_edge
                    s.append((distance[nbr], nbr))
        # Single Source Shortest Distance to all other nodes
        for i in range(len(self.vertices)):
            print("Node i", i, "Distance", distance[i])

        return distance[dest]


class DirectedGraph:

    def __init__(self, v):
        self.total_vertices: int = v
        self.vertices = {i: set() for i in range(v)}

    def add_edge(self, i: int, j: int):
        self.vertices[i].add(j)

    def dfs(self, source, visited, stack):
        # Arrive Node
        visited[source] = True
        stack[source] = True

        # Do some work at node, return True if backedge is found here itself
        for nbr in self.vertices[source]:
            if stack[nbr]:
                return True
            elif not visited[nbr]:
                nbr_found_a_cycle = self.dfs(nbr, visited, stack)
                if nbr_found_a_cycle:
                    return True

        # going back
        stack[source] = False
        return False

    def is_contains_cycle(self):
        visited = [False] * self.total_vertices
        stack = [False] * self.total_vertices

        for i in range(self.total_vertices):
            if not visited[i]:
                if self.dfs(i, visited, stack):
                    return True
        return False
