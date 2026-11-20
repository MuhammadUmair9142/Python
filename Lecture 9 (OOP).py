# class Employee:
#     # Attributes
#     name = ''
#     email = ''
#     salary = 0
#     # methods / function
#     def details(self):
#         print(f"Name: {self.name}\nEmail: {self.email}\nSalary:{self.salary}")


# #object
# emp = Employee()
# emp.details()


# class Employee:
#     # Attributes
#     name = ''
#     email = ''
#     salary = 0
#     # methods / function
#     def details(self):
#         print(f"Name: {self.name} \nEmail: {self.email} \nSalary:{self.salary}")


# #object
# emp = Employee()
# emp.name = "Waqar"
# emp.email = "waqar@gmail.com"
# emp.salary = 70000
# emp.details()

# emp1 = Employee()
# emp1.name = "Zain"
# emp1.email = "zain@gmail.com"
# emp1.salary = 50000
# emp1.details()


# class Employee:
#     # Attributes
#     name = ''
#     email = ''
#     salary = 0
#     # methods / function
#     def details(self,full_name,new_email,_amount):

#         self.name = full_name
#         self.email = new_email
#         self.salary = _amount
#         print(f"Name: {self.name} \nEmail: {self.email} \nSalary:{self.salary}")


# #object
# emp = Employee()
# emp.details('Hassam','hassam@gmail.com',60000)
# print(emp.name)

#Constructor
# class product:
#     def __init__(self,name,price,color):
#         print(f"Name: {name} Price: {price} color:{color}")


# products = product("Shirt",1000,"Black")




# class Vehicle:
#     name = ''
#     model = ''
#     color = ''
#     # methods / function
#     def details(self,vehicle_name,vehicle_model,vehicle_color):

#         self.name = vehicle_name
#         self.email = vehicle_model
#         self.salary = vehicle_color
#         print(f"Vehicle Name: {self.name} \nModel: {self.email} \nColor: {self.salary}")

# emp = Vehicle()
# emp.details('Honda','70cc',"black")


class Vehicle:
    def __init__(self,vehicle_name,vehicle_model,vehicle_color):
        print(f"Name: {vehicle_name} \nPrice: {vehicle_model} \ncolor:{vehicle_color}")


Vehicles = Vehicle("Honda","70cc","black")