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
    #chinese postman problem

    list(nx.eulerian_circuit(edge_map))
    
    #print(edge_map)
    graph_network.DrawGraph(G_map,edge_map)
    

if __name__ == "__main__":
    main()


