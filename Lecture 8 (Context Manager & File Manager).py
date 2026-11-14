#File Handling
#create and write

# file = open('text.txt','w')
# file.write('\nThis is our Secpnd line in our text file')
# file.close

#read File

# f = open("text.txt","r")
# print(f.read())
# f.close()

#append line

# f = open("text.txt","a")
# f.write('This is the appended line')
# f.close()

#Context Manager
# with open('new.txt',"w") as file:
#     file.write('How are you?')

# with open('new.txt',"r") as file:
#     print(file.read())

# def read_log(file_path):
#     with open(file_path,"r") as file:
#         for f in file:
#             yield f


# for log in read_log('log.txt'):
#     if "ERROR" in log:
#         print(log)


