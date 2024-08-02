# for i in range(1,10):
#     if i==4:
#         break
#     print(i)


 #continue
# i=1
# while i<=10:
#      if i==7:
#          continue
#      print(i)
#      i+=1


# a=[1,2,3,4,5]
# print(len(a))   
# print(sum(a)) 


# a=[1,2,3,4,5,6]
# b=[99,100]
# a.append(7) #append 
# print(a)
# a.insert(2,44)  #insert
# print(a)
# a.extend(b)  #extend
# print(a)

# a.remove(5)  #5 index will be removed   # remove
# print(a)
# a.pop(2)  #2 index will pop    #pop
# print(a)
# #a.clear() #clear
# #print(a)

# print(a.index(3))   #index 
# print(a.count(99))  #count

# a=[1,2,3,4,5,6] #copy
# b=[99,100]
# c=a.copy()
# print(c)
# print(a)

#slicing
# a=[1,2,3,4,5,6,7,8,9,10]

# print(a[:])
# print(a[:7])
# print(a[:7:2])
# print(a[::-1])

# a=(1,2,3,4)
# print(type(a))
# b=("raj",)  #, for adding two tuples
# print(type(b))
# c=a+b  
# print(c)

# a=(1,2,3,4)
# b=list(a)  #list datastructure
# b.insert(3,9)
# b=tuple(b)
# print(b)

#sets
# a={1,2,3,4,5,6,7,8,9,10,11,22,"roy","raj"}
# b={"apple","orange",2,3,4}
# # print(a)
# # a.add(44) #for add value
# # print(a)
# c=a.union(b) #join write only once
# print(c)
# d=a.intersection(b) #print common 
# print(d)


#dictionaries
# data={"name":"Divyansh","age":17,"branch":"IF"}
# print(data)
# print(data.keys()) #only keys
# print(data.values()) #only values
# print(data.items()) #for keys and values

# data["address"]="borivali"
# print(data)
# data.update({'address': 'andheri'})
# print(data)


#def
# def greet(name):
#     print("hello ",name)
#     print("good morning")

# greet("rahul")


# def square(num):
#     return num**2

# res=square(89)
# print(res)

#example of average in def
age=[1,2,3,4,5]
average=(1,2,3,4,5)

def average(*age):
    total=0
    for i in range(len(age)+1):
        total+=i
        print(total)
    return total/len(age)

ages=average(1,2,3,4,)
print(ages)

# average(a)

# def average(ages):
#     return sum(ages)/len(ages)
# age=[1,2,3,4,5]
# average(age)
# print(age)





































