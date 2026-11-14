# #Generator 

# def count_up_to(n):
#     count = 1
#     while count <= n: 
#         yield count
#         count += 1

# numbers = count_up_to(20)

# # print(next(numbers))


# for i in range (50):
#     print(next(numbers))

# Task:

# def count_up_to (n):
#     lists = ["umair","osama","uzair"]

#     for li in lists:
#         yield li


#Decorator:

# def decorator(func):
#     def wrapper():
#         print("Something run before funtion")
#         func()
#         print("Something run after funtion")
#     return wrapper


# @decorator
# def say_hello():
#     print("Hello how are you?")

# say_hello()


# def check_login(func):
#     def wrapper(password):
#         if password == "admin123":
#             func(password)
#         else:
#             print("Access Denied")
#     return wrapper

# # @check_login
# def dashboard(user):
#     print("welcome to the dashboard")

# dashboard = check_login(dashboard)
# dashboard("admin1234")

# def check_login(func):
#     def wrapper(password):
#         if password == "admin123":
#             func(password)
#         else:
#             print("Access Denied")
#     return wrapper

# @check_login
# def dashboard(user):
#     print("welcome to the dashboard")

# dashboard ("admin123")

def check_login(func):
    def wrapper(age, testPassed):
        if age >= "18" and testPassed == True:
            func(age)
        else:
            print("You are not eligible for now")
    return wrapper

@check_login
def dashboard(age):
    print("welcome to the School")

dashboard("19",testPassed=False)

