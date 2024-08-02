#how to take input from user in lists
#listy=[]
# n=int(input("enter size:"))
# for i in range(n):
#     a-int(input(f"enter element {i+1}"))
#     listy.append(a)
#     print(listy)

#list comprehension
# listy=[i for i in range(100)]  #for print 100 
# print(listy)

#for print square of 1 to 10
# listy=[i**2 for i in range(10)]
# print(listy)

# listy=[i for i in range(10) if i!=6]
# print(listy)

# list=[i for i in range(10) if i%2==0]
# print(list)

#for dictionaries comprehension
# data={i:i for i in range(10)}
# print(data)

# data={i:i**2 for i in range(10)}
# print(data)

# data={i:i**2 for i in range(10) if i!=6}
# print(data)

# data={i:i for i in "pranav"}
# print(data)

# data={i:i for i in range(int(input("enter start:")),int(input("enter end:")),int(input("enter step:")))}
# print(data)  #range function

#function with parameters
# def data(name,age):
#     print(f"my name is {name}, i am {age} year old")

# data(age=15,name="leo")

#function arguments
# def data(name="none",age=0):
#      print(f"my name is {name}, i am {age} year old")

# data()


#keyword arguments
# def bill(**total):
#     sum=0
#     for key,value in total.items():
#         print(key,value)
#         sum+=value
#     print("total bill",sum)

# bill(milk=28,bread=34,egg=29)


#recursive function
# def factorial(x):
#     """"this is a recursive function to find the factorial of an integer"""

#     if x == 1:
#         return 1
#     else:
#         return(x*factorial(x-1))
    
# num = 3
# print("the factorial of",num,"is",factorial(num))


#lambda function
# p=lambda x:x**2
# print(p(5))

#oops
# class Parrot():
#     color="green"

#     def voice(self):
#         print("tweet tweet")

# obj=Parrot()
# print(obj.color)
# print(obj.voice())


#











































































