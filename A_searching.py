import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        self.g = g  # Cost from start node
        self.h = h  # Heuristic cost
        self.f = g + h  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def astar(tree, start, goal, heuristic_values):
    start_node = Node(start, g=0, h=heuristic_values.get(start, float('inf')))
    goal_node = Node(goal)

    open_list = []
    closed_list = set()

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.name)

        if current_node.name == goal_node.name:
            return reconstruct_path(current_node)

        for (child_name, cost) in tree.get(current_node.name, []):
            if child_name in closed_list:
                continue

            g = current_node.g + cost
            h = heuristic_values.get(child_name, float('inf'))
            child_node = Node(child_name, current_node, g, h)

            if not any(node.name == child_node.name and node.f <= child_node.f for node in open_list):
                heapq.heappush(open_list, child_node)

    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    return path[::-1]

def get_user_input():
    tree = {}
    heuristic_values = {}

    print("Enter the tree connections (parent -> child, cost). Type 'done' when finished:")
    while True:
        connection = input("Format: parent child cost (e.g., A B 1): ")
        if connection == "done":
            break
        parent, child, cost = connection.split()
        cost = int(cost)
        if parent not in tree:
            tree[parent] = []
        tree[parent].append((child, cost))

    print("Enter the heuristic values (node h_value). Type 'done' when finished:")
    while True:
        h_value = input("Format: node h_value (e.g., A 7): ")
        if h_value == "done":
            break
        node, h = h_value.split()
        heuristic_values[node] = int(h)

    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")

    return tree, start, goal, heuristic_values

# Running the code
tree, start, goal, heuristic_values = get_user_input()
path = astar(tree, start, goal, heuristic_values)

if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found")
