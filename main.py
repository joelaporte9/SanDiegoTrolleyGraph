from Trolley import Trolley
import networkx as nx
from GraphTrolley import GraphTrolley

starting_point = "utcS"

def main():
    # Load trolley stops from the data file
    graph_network = GraphTrolley()

    #print(graph_network.NetworkCoords())
    G_map = graph_network.GraphNetwork()

    edge_map = nx.bfs_tree(G_map, source=starting_point)
    print(list(edge_map.edges()))
    #MAKE BFS FUNCTION

    visited = set() # Set to keep track of visited nodes of edge_map.

    def dfs(visited, edge_map, node):  #function for dfs 
        if node not in visited:
            print (node)
            visited.add(node)
            for neighbour in edge_map[node]:
                
                dfs(visited, edge_map, neighbour)

    print("Following is the Depth-First Search")
    dfs(visited, edge_map, starting_point)  # Add child nodes to stack

    #print(edge_map)
    graph_network.DrawGraph(G_map,edge_map)
    

if __name__ == "__main__":
    main()


