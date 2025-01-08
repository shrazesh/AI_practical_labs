def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()  # Set to keep track of visited nodes
    
    visited.add(start_node)  # Mark the current node as visited
    dfs_order.append(start_node)  # Add the current node to the DFS traversal order
    
    # Visit all unvisited neighbors recursively
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def main():
    graph = {}
    num_nodes = int(input("Enter the number of nodes in the graph: "))

    # Input the graph connections
    for _ in range(num_nodes):
        node = input("Enter the node: ")
        neighbors = input(f"Enter the neighbors of {node} separated by space: ").split()
        graph[node] = neighbors

    start_node = input("Enter the starting node for DFS: ")
    
    global dfs_order
    dfs_order = []  # List to store the DFS traversal order
    
    # Perform DFS
    dfs(graph, start_node)
    
    # Display the DFS traversal order
    print(f"DFS traversal starting from node {start_node}: {' -> '.join(dfs_order)}")

if __name__ == "__main__":
    main()
