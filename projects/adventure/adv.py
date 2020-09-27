from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

"""
graph should look like this
{
  0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}

{
  0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
  5: {'n': 0, 's': '?', 'e': '?'}
}

"""
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.
traversal_path = []
class Graph:
    def __init__(self):
        self.vertices = dict()
        self.visited = set()

    def build_vertices(self, graph):
        for room in graph:
            # print(room)
            self.vertices[room] = {}
            if "n" in graph[room][1]:
                self.vertices[room]["n"] = "?"
            if "s" in graph[room][1]:
                self.vertices[room]["s"] = "?"
            if "e" in graph[room][1]:
                self.vertices[room]["e"] = "?"
            if "w" in graph[room][1]:
                self.vertices[room]["w"] = "?"

    def dft(self, starting_room):
        stack = []
        stack.append(starting_room)
        # print(starting_room)
        while len(stack) > 0:
            cur_node = stack.pop()
            # print(cur_node)
            if cur_node not in self.visited:
                # print(cur_node)
                self.visited.add(cur_node)
                neighbors = self.vertices[player.current_room.id]
                # print(neighbors)
                if "n" in neighbors and neighbors["n"] == "?":
                    traversal_path.append("n")
                    self.add_direction(cur_node, "n")
                    stack.append(player.current_room.id)
                elif "s" in neighbors and neighbors["s"] == "?":
                    traversal_path.append("s")
                    self.add_direction(cur_node, "s")
                    stack.append(player.current_room.id)
                elif "w" in neighbors and neighbors["w"] == "?":
                    traversal_path.append("w")
                    self.add_direction(cur_node, "w")
                    stack.append(player.current_room.id)
                elif "e" in neighbors and neighbors["e"] == "?":
                    traversal_path.append("e")
                    self.add_direction(cur_node, "e")
                    stack.append(player.current_room.id)
        self.bfs(player.current_room.id)
        

    def bfs(self, current_room):
        # print(current_room)
        dir_dict = {}
        queue = []
        revisit = set()
        queue.insert(0, [current_room])
        while len(queue) > 0:
            cur_path = queue.pop()
            cur_room = cur_path[-1]
            # print(cur_path)
            print(cur_room)
            edges = self.vertices[cur_room]
            # print(edges)
            if "n" in edges and edges["n"] == "?":
                # print(cur_path)
                # print(dir_dict)
                i = 0
                while i < len(cur_path) - 1:
                    self.add_direction(cur_path[i], dir_dict[cur_path[i+1]])
                    traversal_path.append(dir_dict[cur_path[i+1]])
                    i += 1
                print(dir_dict)
                self.visited.remove(cur_path[-1])
                self.dft(cur_path[-1])
                return
            elif "s" in edges and edges["s"] == "?":
                # print(cur_path)
                # print(dir_dict)
                i = 0
                while i < len(cur_path) - 1:
                    self.add_direction(cur_path[i], dir_dict[cur_path[i+1]])
                    traversal_path.append(dir_dict[cur_path[i+1]])
                    i += 1
                print(dir_dict)
                self.visited.remove(cur_path[-1])
                self.dft(cur_path[-1])
                return
            elif "e" in edges and edges["e"] == "?":
                # print(cur_path)
                # print(dir_dict)
                i = 0
                while i < len(cur_path) - 1:
                    self.add_direction(cur_path[i], dir_dict[cur_path[i+1]])
                    traversal_path.append(dir_dict[cur_path[i+1]])
                    i += 1
                print(dir_dict)
                self.visited.remove(cur_path[-1])
                self.dft(cur_path[-1])
                return
            elif "w" in edges and edges["w"] == "?":
                # print(cur_path)
                # print(dir_dict)
                i = 0
                while i < len(cur_path) - 1:
                    self.add_direction(cur_path[i], dir_dict[cur_path[i+1]])
                    traversal_path.append(dir_dict[cur_path[i+1]])
                    i += 1
                print(dir_dict)
                self.visited.remove(cur_path[-1])
                self.dft(cur_path[-1])
                return
            if cur_room not in revisit:
                revisit.add(cur_room)
                for neighbor in edges:
                    path_copy = list(cur_path)
                    print(f"Neighbor: {neighbor}")
                    if self.vertices[cur_room][neighbor] not in dir_dict:
                        dir_dict[self.vertices[cur_room][neighbor]] = neighbor
                    print(dir_dict)
                    path_copy.append(self.vertices[cur_room][neighbor])
                    queue.insert(0, path_copy)

    def add_direction(self, current_room, direction):
        last_room = player.current_room.id
        player.travel(direction)
        self.vertices[last_room][direction] = player.current_room.id
        if direction == "n":
            self.vertices[player.current_room.id]["s"] = last_room
        if direction == "s":
            self.vertices[player.current_room.id]["n"] = last_room
        if direction == "e":
            self.vertices[player.current_room.id]["w"] = last_room
        if direction == "w":
            self.vertices[player.current_room.id]["e"] = last_room

maze = Graph()
maze.build_vertices(room_graph)
maze.dft(world.starting_room.id)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
