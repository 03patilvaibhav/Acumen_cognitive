

speed_limit = 60
traffic_light = "Green"
class Vehicle :
    def start_engine(self):
        message = "Engine started"  # Local variable
        print(message)
    
    
    
class Car(Vehicle) :   
    def __init__(self, make):
        self.make = make  # Object variable

    def start_engine(self):
        message = "Car engine started"  # Local variable
        print(message)

class Bike(Vehicle):
    def __init__(self, bike_type):
        self.type = bike_type  # Object variable

    def start_engine(self):
        message = "Bike engine started"  # Local variable
        print(message)

def inheritance_and_polymorphism():
    vehicle = Vehicle()
    car = Car("Honda")
    bike = Bike("Cruise")

    # List of vehicles
    vehicles = [vehicle, car, bike]

    for i in vehicles:
        i.start_engine()

if __name__ == "__main__":
    print(f"Global variable traffic_light: {traffic_light}")
    print(f"Module-level variable speed_limit: {speed_limit}")
    inheritance_and_polymorphism()