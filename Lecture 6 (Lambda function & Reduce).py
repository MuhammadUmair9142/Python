# #Lambda function
# add = lambda a,b: a+b

# print(add(2,9))

# # Lambda with map function
# numbers = [1,2,3,4,5] #List

# result = list(map(lambda a:a*2,numbers))
# print(result)

# Lambda with filter function
# num = [1,2,3,4,5,6,7,8,9,10] #List

# evenNumbers = list(filter(lambda a:a%2 == 0,num))
# print(evenNumbers)

# oddNumbers = list(filter(lambda a:a%2 != 0,num))
# print(oddNumbers)

from functools import reduce

nums=[1,2,3,4,5,6]

results=reduce(lambda a,b:a+b,nums)
print(results)


orders=[
    {"product":"Shirt","price":2000,"qty":1,"discount":True},
    {"product":"Shoes","price":10000,"qty":1,"discount":False},
    {"product":"Cap","price":200,"qty":1,"discount":True}
]

discount_orders=list(filter(lambda ord:ord["discount"]== True,orders))
withOutDiscount = list(filter(lambda ord: ord["discount"] == False, orders))
withOutDiscountCalculated=list(map(lambda ord:(ord["price"] * ord["qty"]),withOutDiscount))
discountCalculated=list(map(lambda ord:(ord["price"] * ord["qty"]) *0.9,discount_orders))
totalAmount=reduce(
    lambda total,price: total+price+withOutDiscountCalculated,
    discountCalculated
)

print("total amount",totalAmount)