#oop concept (n-capsulation,abstraction)
# class Car():
#     def __init__(self,model,color):  #constructor
#         self.model=model   #function
#         self.color=color
#         self.__speed=0

#     def accelerate(self,increment):
#         self.__speed+=increment

#     def brake(self,decrement):
#         self.__speed-=decrement

#     def get_speed(self):
#         return self.__speed
    

# obj=Car("BMW","black")
# obj.accelerate(30)
# print(obj.get_speed())
# obj.brake(10)
# print(obj.get_speed())
# print(obj._Car__speed)


#single ineheretence
# class Animal():
#     def speak(self):
#         print("animal is speaking")

# class Dog(Animal):
#     def bark(self):
#         print("animal is barking")

# obj=Dog()
# obj.speak()
# obj.bark()


#multilevel inheritence
#class Animal():
#     def speak(self):
#         print("animal is speaking")

# class Dog(Animal):
#     def bark(self):
#         print("animal is barking")

# class Puppy(Dog):
#     def weeep(self):
#         print("dogb is weeping")

# obj=Puppy()
# obj.speak()
# obj.bark()

#single level inheritence example
# class Animal():
#     def __init__(self,species):
#         self.species = species

#     def speak(self):
#         print(f"{self.species} speaks")

# class Dog(Animal):
#      def __init__(self, species, breed):
#          super().__init__(species)
#          self.breed = breed

#      def bark(self):
#          print(f"{self.species} ({self.breed}) barks")

# obj = Dog("Dog", "Labrador")

# obj.speak()
# obj.bark()


# multiple inheritence
# class Parent1:
#     def p1(self):
#         print("p1")
        
# class Parent2:
#     def p2(self):
#         print("p2")

# class Child(Parent1,Parent2):
#     def whoami(self):
#         print("i am child of")

# obj=Child()
# obj.whoami()
# obj.p1()
# obj.p2()


#single inheritence example
# class Bird:
#     def __init__(self):
#         print("Bird id ready")

# class Penguin(Bird):
#     def __init__(self):
#         super().__init__()
#         print("penguin is ready")

# peggy = Penguin()


#overriding
# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year

# class Car(Vehicle):
#     def mov(self):
#         print("Move!")

# class Boat(Vehicle):
#     def mov(self):
#         print("sail!")

# class Plane(Vehicle):
#     def mov(self):
#         print("Fly!")

# car1 = Car("ford","2014")
# boat1 = Boat("speed","2020")
# plane1 = Plane("fighter","2022")

# for x in (car1,boat1,plane1):
#     print(x.brand)
#     print(x.year)
#     x.mov()


#overloading
# class Demo():
#     def add2(self,a,b):
#         return a+b 
#     def add2(self,a,b,c):
#         return a+b+c
    
# obj=Demo()
# print(obj.add2(2,3))
#print(obj.add2(2,3,5))

# file=open("demo.txt","w")
# file.write("hello this is my file")
# file.close()

# with open("example.txt","w") as file:
#     file.write("hello!")

# with open("example.txt","r") as file:
#     content=file.read()
#     print(content)

# with open("example.txt","a") as file:
#     file.write('\nappended line')


# with open("example.txt","r") as file:
#     print("\nReading line by line:")
#     for line in file:
#         print(line.strip())

# with open("example.txt","r") as file:
#     file.seek(3)
#     print("\nReading from 3rd character onwards:")
#     remaining_content = file.read()
#     print(remaining_content)


# with open("example.txt","r+") as file:
#     file.write("New content written in r+ mode.")
#     file.seek(0)
#     con=file.read()
#     print(con)
# with open("demo.txt","w+") as file:
#     file.write("Content written in w+ mode.")
#     file.seek(0)
#     content = file.read()
#     print(content)

with open("example.txt","a+") as file:
    file.write("\nappend")
    file.seek(0)
    con=file.read()
    print(con)
    









