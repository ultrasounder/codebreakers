# class Dog:
#     pass

# myDog = Dog()

# class Dog:
#     def __init__ (self, name, age):
#         self.name = name #same as constructor syntax in Java where we initalize instance variables with some default values
#         self.age = age

# my_dog = Dog("Snoopy", 8)
# print(my_dog.name) #call the instance method on the object
# print(my_dog.age) 

class Dog:
    #Class attribute
    species = "mammal"
    #Initializer instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
    #instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    
    #instantiate a dog object
mikey = Dog("Mikey", 6)
print(mikey.description())
print(mikey.speak("Gruf Gruff"))

#Beagle inherits from dog
class Beagle(Dog):
    def run(self, speed):
        return "{}, the beagle, runs {}".format(self.name, speed)

snoopy = Beagle("snoopy", 8)
print(snoopy.description())

print(snoopy.run("fast"))



