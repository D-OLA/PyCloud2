def greet_user():
	print(f"\nHello and welcome to functions in python")

# greet_user()

# def greetings(username):
# 	print(f"Hello, {username.title()}!")
# greetings('david')

def describe_pet(type, name):
	print(f"\nI have a {type}.")
	print(f"\nMy {type}'s name is {name.title()}.\n")
describe_pet(type='Dog', name='Tessy')

def greet_users(names):
	for name in names:
		msg = f"Hello, {name.title()}"
		print(msg)

usernames = ['jane', 'andrew', 'abel']
# greet_users(usernames)

def make_pizza(size, toppings):
	print(f"\nMaking a {size}-inch pizza with the following topping")
	print(f"--{toppings}")

# make_pizza(14, 'Gudu')

# make_pizza(14, 'peppers')
# make_pizza(9, 'onions')