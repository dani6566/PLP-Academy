class Car:
    #Class for a Car
    def move(self):
        return "Driving...  "

class Plane:
    #Class for a Plane
    def move(self):
        return "Flying high... "
        
class Boat:
    #Class for a Boat
    def move(self):
        return "Sailing smoothly..."
    

if __name__ == "__main__":
    # Create a list containing different objects
    transport_vehicles = [Car(), Plane(), Boat()]

    for vehicle in transport_vehicles:
        # (Car, Plane, or Boat) at runtime.
        print(f"A {vehicle.__class__.__name__} says: {vehicle.move()}")
