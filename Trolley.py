import csv

# GLOBAL variables
global san_diego_trolley_data 

#GTFS data provided by the City of Sann Diego
san_diego_trolley_data: str = 'data/TrolleyStops.txt'

class Trolley:
    # initialize the variables of the rows for the data well grab from the txt file
    def __init__(self, stop_id, stop_name, stop_desc, stop_lat, stop_lon):
        self.stop_id: str = stop_id
        self.stop_name: str = stop_name
        self.stop_desc: str = stop_desc
        self.stop_lon: float = stop_lon
        self.stop_lat: float = stop_lat

    # Formatted the results of the txt file 
    def __str__(self) -> str:
        return (f"Stop ID: {self.stop_id}\n \
                Stop Name: {self.stop_name}\n \
                Stop Type:{self.stop_desc}\n \
                Stop Lat: {self.stop_lat}\n \
                Stop Lon:{ self.stop_lon}")   
                 
    # Get function for stop ID
    def get_stop_id(self) -> str:
        return self.stop_id
    
    # Get function for stop name
    def get_stop_name(self) -> str:
        return self.stop_name
    
    # Get function for stop cords
    def get_stop_coordinates(self) -> tuple:
        return (self.stop_lon, self.stop_lat)
        
    # Get function for trolley
    def _trolley(self) -> str:
        return self.trolley
    
    # Read the cords from the test file above
    @staticmethod
    def map_network() -> list:
        trolley_stops: list = []
        with open(san_diego_trolley_data, 'r') as file:
            trolley_txt = csv.reader(file)
            next(trolley_txt)
            for row in trolley_txt:
               # For the first 6 rows in the txt file, assign a column to the variables above ^
               if len(row) >= 6:
                    stop_id = row[0]
                    stop_name = row[2]
                    stop_desc = row[3]
                    stop_lat = float(row[4]) if row[4] else 0.0
                    stop_lon = float(row[5]) if row[5] else 0.0

                    # Trolley object for the data we grabbed from the txt file columns. 
                    trolley_stop = Trolley(
                        stop_id, stop_name, stop_desc, 
                        stop_lat, stop_lon
                    )

                    trolley_stops.append(trolley_stop)
                
            return trolley_stops
    