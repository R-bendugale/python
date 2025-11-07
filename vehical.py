class Vehicle:
    def displayInfo(self, name=None, wheels=None):
        if name is not None and wheels is not None:
            print(f"Vehicle Name: {name}, Wheels: {wheels}")
        elif name is not None:
            print(f"Vehicle Name: {name}")
        else:
            print("No vehicle information available")

v1 = Vehicle()
v1.displayInfo()
v1.displayInfo("Bicycle")
v1.displayInfo("Car", 4)  
