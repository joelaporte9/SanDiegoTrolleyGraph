import matplotlib.pyplot as plt
import networkx as nx

# Import Classes
from Trolley import Trolley

class GraphTrolley:
    san_diego_trolley_edges: str = 'trolley_edges.txt'

    # Test getting geo info
    @staticmethod
    def NetworkCoords() -> dict:
        locations: dict = {}
        trolley_stops: list = Trolley.map_network()  # List of Trolley objects

        for station in trolley_stops:
            # Use the Trolley object's methods correctly
            locations[station.get_stop_id()] = station.get_stop_coordinates()

        return locations

    def GraphNetwork(self):
        # init map
        trolley_map = nx.DiGraph()
        # Initialize lists to store edges and nodes
        self.edges = []  # Store edges for later use in drawing
        self.edge_colors = []  # Store colors for each edge
        self.nodes = set()  # Track nodes to use in drawing

        with open(GraphTrolley.san_diego_trolley_edges, 'r') as file:
            edges_txt = file.readlines()
            for line in edges_txt:
                element = line.strip().split(",")

                #check if the line has 4 elements 
                if len(line) < 4:
                    continue

                #Assign the column of the Edges text file with the coresponding 
                parent_station = element[0]
                destination = element[1]
                time = element[2]
                color = element[3]
                
                # add edge to graph with color attribute and time as weight
                trolley_map.add_edge(parent_station, destination, weight=float(time), color=color) 

                self.edges.append((parent_station, destination))
                self.edge_colors.append(color)

                # Track nodes
                self.nodes.add(parent_station)
                self.nodes.add(destination)
                
        # return graph
        return trolley_map
    
    def DrawGraph(self, G, new_plot=True, title='Map of San Diego Trolley', label=None):
        # Get the coordinates from the trolley stop ID. see NetworkCoords function for more detail.
        cords = GraphTrolley.NetworkCoords()

        if new_plot:
            plt.figure()
            plt.title(title)

        # add labels if specified
        if label is not None:
            nx.draw_networkx_labels(G, pos=cords, labels=label, font_size=6)

        # draw edges with geographic positions and color corresponding to line
        nx.draw_networkx_edges(G, pos=cords, edge_color=self.edge_colors, edgelist=self.edges)

        # draw nodes based on geo positions
        nx.draw_networkx_nodes(G, pos=cords, node_color='black', node_size=20, nodelist=self.nodes)
        
        plt.show()

    def find_eulerian_path(self, G):
        # Check if the graph has an Eulerian path or circuit
        if nx.is_eulerian(G):
            print("The graph has an Eulerian circuit.")
            path = list(nx.eulerian_circuit(G))
        elif nx.has_eulerian_path(G):
            print("The graph has an Eulerian path.")
            path = list(nx.eulerian_path(G))
        else:
            print("The graph does not have an Eulerian path or circuit.")
            return None

        # Print the Eulerian path or circuit
        print("Eulerian Path or Circuit:", path)
        return path

# Example usage
graph_trolley = GraphTrolley()
trolley_map = graph_trolley.GraphNetwork()
graph_trolley.DrawGraph(trolley_map, title="Map of San Diego Trolley")

# Find and print the Eulerian path or circuit
eulerian_path = graph_trolley.find_eulerian_path(trolley_map)
        

        

        
                
                
