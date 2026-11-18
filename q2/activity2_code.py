class Car:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def move(self):
        print("The car drives on the road.")

class Boat:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def move(self):
        print("The boat sails on the water.")

class Drone:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def move(self):
        print("The drone flies in the air.")

def start_trip(self):
    self.vehicle.move()

obj1 = Car(Car())
obj2 = Boat(Boat())
obj3 = Drone(Drone())

obj1.start_trip()
obj2.start_trip()
obj3.start_trip()
