#file handeling 
# with open("demo1.txt","w") as file:
#     file.write("helloo")

# with open("demo1.txt","w") as file:
#     file.write("helloo")


#syntax error
# i=0
# if i==0
#     print("hello")
# else:
#     print("no hello")


#type error
# res=45+"1"
# print(res)


#name error
#print(variable)


#index error
# listy=[1,2,3,4]
# print(listy[4])


#keyerror
# data={1:"apple",2:"orange",3:"grapes"}
# print(data[4])


#value error
# name="Cries"  #if pass str inside int
# print(int(name))


#filenotfound error
# with open("filey.txt","r")as file:
#     content=file.read(10)
#     print(content)


#ZeroDivisionError
# res=11/0
# print(res)


#exception handling
#syntax error
# try:
#     i-0
#     if i>1
#         print("true")
# except SyntaxError as e:
#     print("syntax error encountered",e)
# x="success"
# print(x)


#type error
# try:
#     res=123+"yt"
# except TypeError as e:
#     print("type error encountered:",e)
# x="success"
# print(x)


#name error
# try:
#    print(variable)
# except NameError as e:
#     print("name error encountered",e)
# x="success"
# print(x)


#index error
# try:
#    listy=[1,2,3,4]
#    print(listy[4])
# except IndexError as e:
#     print("index error encountered:",e)
# x="success"
# print(x)


#keyerror
# try:
#     data={1:"apple",2:"orange",3:"grapes"}
#     print(data[4])
# except KeyError as e:
#     print("key error encountered:",e)
# x="success"
# print(x)


#value error
# try:
#     name="Cries"  #if pass str inside int
#     print(int(name))
# except ValueError as e:
#      print("value error encountered:",e)
# x="success"
# print(x)


#filenotfound
# try:
#    with open("filey.txt","r")as file:
#     content=file.read(10)
#     print(content)
# except IOError as e:
#     print("I/O error encountered:",e)
# x="success"
# print(x)


#zerodivision error
# try:
#     res=11/0
#     print(res)
# except ZeroDivisionError as e:
#     print("Zero division error encountered:",e)
# x="success"
# print(x)


#keyboard interrupt
# i=0
# while True:
#     print(i)


#userdefined Error
#keyboardinterrupt
# def get_phone_number():
#     while True:
#         try:
#             phone_number = input("please enter a 10-digit phone number: ")
#             if len(phone_number)!=10:
#                 raise ValueError("phone number must be exactly 10 digits long.") #raise for user defined errror
            
#             if not phone_number.isdecimal():
#                 raise ValueError("phone number must contain only digits.")
#             return phone_number
#         except ValueError as ve:
#             print("invalid input:",ve)

# #example usage
# try:
#     phone_number = get_phone_number()
#     print("phone number entered:", phone_number)
# except KeyboardInterrupt:
#     print("\nProgram terminated by user.")
# except Exception as e:
#     print("an unexpected error occurred:",e)  



# import operation1
# operation1.addition(2,6)

# import operation1
# operation1.subtraction(6,3)


from pack import *
res=mymod.add(2,3)
res1=mymod.sub(5,3)
res2=mymod.mul(5,4)
res3=mymod.div(4,1)
print(res)
print(res1)
print(res2)
print(res3)


