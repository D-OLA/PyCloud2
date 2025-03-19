# class Dog:

# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def sit(self):
# 		print(f"{self.name} is now sitting")

# 	def roll_over(self):
# 		print(f"{self.name} rolled over!")

# my_dog = Dog('Tessy', 4)
# your_dog = Dog('Tom', 5)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()

# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.roll_over()

class Resturant:

	def __init__(self, name, type):
		self.name = name
		self.type = type

	def describe(self):
		print(f"\nThe resturant called {self.name} is a {self.type} resturant !")

	def open(self):
		print(f"This {self.type} resturant is currently open")

resturant = Resturant('La Cartel', 'Fastfood')

resturant.describe()
resturant.open() 

# Now learn how to test functions and classes as we code

