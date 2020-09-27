"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def delete_vertex(self, vertex_id):
        ## delete the key-value pair
        ## find all references to the vertex
        pass
        

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()
        while queue.size() > 0:
            cur_node = queue.dequeue()
            if cur_node not in visited:
                print(cur_node)
                visited.add(cur_node)
                neighbors = self.get_neighbors(cur_node)
                for neighbor in neighbors:
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() > 0:
            cur_node = stack.pop()
            if cur_node not in visited:
                print(cur_node)
                visited.add(cur_node)
                neighbors = self.get_neighbors(cur_node)
                for neighbor in neighbors:
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)
        visited.add(starting_vertex)
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # begin at starting vertex
        # explore vertex
        ## while +1 unscheduled vertices adjacent
        ### schedule adjacent vertext to be explored
        ### queue
        ## mark vertex as explored
        queue = Queue()
        visited = set()
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            cur_path = queue.dequeue()
            cur_word = cur_path[-1]
            if cur_word == destination_vertex:
                return cur_path
            if cur_word not in visited:
                visited.add(cur_word)
                neighbors = self.get_neighbors(cur_word)
                for neighbor in neighbors:
                    #cur_path = cur_path + [neighbor]
                    path_copy = list(cur_path)
                    path_copy.append(neighbor)
                    queue.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # alt answer
        # stack = Stack()
        # result = []
        # stack.push(starting_vertex)
        # visited = set()
        # while stack.size() > 0:
        #     cur_node = stack.pop()
        #     if cur_node not in visited and cur_node is not destination_vertex:
        #         result.append(cur_node)
        #         visited.add(cur_node)
        #         neighbors = self.get_neighbors(cur_node)
        #         for neighbor in neighbors:
        #             stack.push(neighbor)
        #     elif cur_node is destination_vertex:
        #         result.append(cur_node)
        #         return result
        stack = Stack()
        visited = set()
        stack.push([starting_vertex])
        while stack.size() > 0:
            cur_path = stack.pop()
            cur_word = cur_path[-1]
            if cur_word == destination_vertex:
                return cur_path
            if cur_word not in visited:
                visited.add(cur_word)
                neighbors = self.get_neighbors(cur_word)
                for neighbor in neighbors:
                    #cur_path = cur_path + [neighbor]
                    path_copy = list(cur_path)
                    path_copy.append(neighbor)
                    stack.push(path_copy)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited = set(), path=Stack()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if path.size() == 0:
            path.push([starting_vertex])
        visited.add(starting_vertex)
        cur_path = path.pop()
        if starting_vertex == destination_vertex:
            return cur_path
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                path_copy = list(cur_path)
                path_copy.append(neighbor)
                path.push(path_copy)
                result = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if result is not None:
                    return result 
                    


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
