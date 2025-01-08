import heapq

class Node:
    def __init__(self, name, heuristic_value):
        self.name = name
        self.heuristic_value = heuristic_value
        self.parent = None

    def __lt__(self, other):
        return self.heuristic_value < other.heuristic_value

class GreedyBestFirstSearch:
    def __init__(self):
        self.graph = {}
        self.visited = set()

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append(node2)

    def greedy_best_first_search(self, start, goal):
        open_list = []
        heapq.heappush(open_list, Node(start, self.graph[start]['heuristic']))
        self.visited.add(start)

        while open_list:
            current_node = heapq.heappop(open_list)
            print(f"Visiting node {current_node.name} with heuristic value {current_node.heuristic_value}")
            
            if current_node.name == goal:
                print("Goal reached!")
                path = []
                while current_node:
                    path.append(current_node.name)
                    current_node = current_node.parent
                return path[::-1]  # Return reversed path (from start to goal)

            for neighbor in self.graph[current_node.name]['neighbors']:
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    neighbor_node = Node(neighbor, self.graph[neighbor]['heuristic'])
                    neighbor_node.parent = current_node
                    heapq.heappush(open_list, neighbor_node)

        return None  # Return None if goal is not reachable

def get_input():
    # Input the graph
    num_nodes = int(input("Enter the number of nodes: "))
    graph = {}
    
    for i in range(num_nodes):
        node_name = input(f"Enter the name of node {i + 1}: ")
        heuristic_value = int(input(f"Enter heuristic value for node {node_name}: "))
        graph[node_name] = {'heuristic': heuristic_value, 'neighbors': []}
    
    return graph

if __name__ == "__main__":
    # Get user input for graph and heuristic values
    graph_data = get_input()

    # Manually add the neighbors (edges) here:
    graph_data['A']['neighbors'] = ['B', 'C']
    graph_data['B']['neighbors'] = ['A', 'D']
    graph_data['C']['neighbors'] = ['A', 'D']
    graph_data['D']['neighbors'] = ['B', 'C']
    
    # Get the start and goal nodes from the user
    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")

    # Initialize and set up the Greedy Best-First Search
    greedy_search = GreedyBestFirstSearch()
    greedy_search.graph = graph_data
    
    # Perform the search
    result = greedy_search.greedy_best_first_search(start, goal)

    if result:
        print("Path found:", " -> ".join(result))
    else:
        print("No path found from start to goal.")
