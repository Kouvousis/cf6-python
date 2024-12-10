class Vehicle:
    def drive(self):
        raise NotImplementedError("subclasses should implement 'drive' method")
    
class Car(Vehicle):
    def drive(self):
        print("Driving a car.")
        
class Bicycle(Vehicle):
    def drive(self):
        print("Driving a bicycle.")

class HoverBoard:
    def drive(self):
        print("Hovering on a hoverboard.")

class Boat(Vehicle):
    def sail(self):
        print("SAling a boat.")
        
def drive_vehicle(vehicle):
    try:
        vehicle.drive()
    except NotImplementedError:
        print(f"{vehicle.__class__.__name__} cant drive")
        
def main():
    my_car = Car()
    my_bicycle = Bicycle()
    my_hoverboard = HoverBoard()
    my_boat = Boat()
    
    drive_vehicle(my_car)
    drive_vehicle(my_bicycle)
    drive_vehicle(my_hoverboard)
    
    try:
        drive_vehicle(my_boat)
    except NotImplementedError as e:
        print(e)
    

if __name__ == "__main__":
    main()