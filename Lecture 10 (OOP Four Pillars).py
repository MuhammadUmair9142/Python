# class Vehicle:
#     # name = ""         #Not important to write
#     # model = ""        #Not important to write
#     # brand = ""        #Not important to write
    
#     def __init__ (self,brand,name,model):
#         self.brand = brand
#         self.name = name
#         self.model = model

#     def drive(self):
#         print(f"Name:{self.name},\nModel:{self.model},\nBrand:{self.brand}")

# class Car(Vehicle):
#     def seats(self):
#         print("7 Seater")

# car = Car("Toyota","gli",2026)
# car.drive()
# car.seats()

# class Bus(Vehicle):
#     def Space(self):
#         print("40 Seates are available")

# bus = Bus("abcName","defModel",2026)
# bus.drive()




class Vehicle:
    
    def __init__ (self,brand,name,model):
        self.brand = brand
        self.name = name
        self.model = model

    def drive(self):
        print(f"Name:{self.name},\nModel:{self.model},\nBrand:{self.brand}")

class Car(Vehicle):
    def seats(self,total_seats):
        print(f"{total_seats} Seater")

car = Car("Toyota","gli",2026)
car.drive()
car.seats(7)



