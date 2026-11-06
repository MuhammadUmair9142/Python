# products=[]

# products.append('LED')
# products.append('Keyboard')
# products.append('Mouse')
# products.pop(2)

# print(products)


# square=[]

# for i in range(10):
#     square.append(i)

# print(square)

# def sum_numbers(*args):
#     total=0
#     for num in args:
#         total+=num
#     print(total)


# sum_numbers(2,33,42,23)


def studen_info(**kwargs):

    
    for key,value in kwargs.items():   
        print(key, ':' ,value)


studen_info(name='Umair', age=21)