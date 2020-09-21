class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def get_ancestors(ancestors, node):
    valid_ancestors = []
    for ancestor in ancestors:
        if ancestor[1] == node:
            valid_ancestors.append(ancestor[0])
    return valid_ancestors

def earliest_ancestor(ancestors, starting_node):
    queue = Queue()
    queue.enqueue(starting_node)
    result = 0
    visited = set()
    while queue.size() > 0:
        cur_node = queue.dequeue()
        if cur_node not in visited:
            visited.add(cur_node)
            result = cur_node
            neighbors = get_ancestors(ancestors, cur_node)
            ancestor = 999
            i = 0
            if len(neighbors) > 1:
                while i < len(neighbors):
                    if neighbors[i] < ancestor:
                        ancestor = neighbors[i]
                    i += 1
                queue.enqueue(ancestor)
            elif len(neighbors) == 1:
                neighbor = neighbors.pop()
                queue.enqueue(neighbor)   
    if result != starting_node:
        return result
    else:
        return -1