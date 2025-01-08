from collections import deque

def bfs(graph, start_node):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start_node])  # Queue to keep track of nodes to visit
    bfs_order = []  # List to store the BFS traversal order

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            # Add all unvisited neighbors to the queue
            queue.extend([neighbor for neighbor in graph[node] if neighbor not in visited])

    return bfs_order

def main():
    graph = {}
    num_nodes = int(input("Enter the number of nodes in the graph: "))

    # Input the graph connections
    for _ in range(num_nodes):
        node = input("Enter the node: ")
        neighbors = input(f"Enter the neighbors of {node} separated by space: ").split()
        graph[node] = neighbors

    start_node = input("Enter the starting node for BFS: ")
    
    # Perform BFS
    bfs_result = bfs(graph, start_node)
    
    # Display the BFS traversal order
    print(f"BFS traversal starting from node {start_node}: {' -> '.join(bfs_result)}")

if __name__ == "__main__":
    main()
