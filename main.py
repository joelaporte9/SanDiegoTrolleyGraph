from Trolley import Trolley
import networkx as nx
from GraphTrolley import GraphTrolley


def main():
    # Load trolley stops from the data file
    graph_network = GraphTrolley()

    #print(graph_network.NetworkCoords())
    G_map = graph_network.GraphNetwork()

    #draw map of the T with colors corresponding to lines
    edge_map, colors = zip(*nx.get_edge_attributes(G_map,'color').items())
    graph_network.DrawGraph(G_map,edge_map, colors)
    

if __name__ == "__main__":
    main()
