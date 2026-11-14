# #while loop

# number = 0
#     #11<=10 exit

# while number>=-10:
#     print(number)
#     number-=1

# number = 0
#     #11<=10 exit

# while number<=+10:
#     print(number)
#     number+=1


#match case

# command ='stop'

# match command:
#     case 'start':
#         print("starting")
#     case 'stop':
#         print("stopping")
#     case _:
#         print("invalid input")

# day = 'Tuesday'

# match day:
#     case "Monday":
#         print("Today is Monday")
#     case "Tuesday":
#         print("Today is Tuesday")
#     case "wednesday":
#         print("Today is wednesday")
#     case "thursday":
#         print("Today is thursday")
#     case "friday":
#         print("Today is friday")
#     case "saturday":
#         print("Today is saturday")
#     case "weekend":
#         print("Today is weekend")
#     case _:
#         print("unknown")


day = input("Enter day: ").lower()

match day:
    case "monday":
        print("Today is Monday")
    case "tuesday":
        print("Today is Tuesday")
    case "wednesday":
        print("Today is Wednesday")
    case "thursday":
        print("Today is Thursday")
    case "friday":
        print("Today is Friday")
    case "saturday":
        print("Today is Saturday")
    case "sunday":
        print("Today is Sunday")
    case _:
        print("Unknown day")
