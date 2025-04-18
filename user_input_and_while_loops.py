# prompt = "If we know who you are our responses can be better customized"
# prompt += "\nWhat is your full name: "

# name = input(prompt)
# print(f"\nHello, {name}")

height = input("How tall are you in inches: ")
height = int(height)

if height >= 60:
	print("\nYes! You are old enough for this\n")
else:
	print("\nYou're still just a child... try enlisting again next year\n")

# prompt2 = '\nwhat kind of car would you like: '
# carType = input(prompt2.title())
# print(f"\nLet me see if i can find you a {carType}")

prompt3 = "\nhow many people are in your dinner group: "
dinnersize = input(prompt3.title())
dinnersize = int(dinnersize)
if dinnersize > 8:
	excuse = "\nYou'll have to wait for a table"
	print(excuse.title())
else:
	print(f"\nplease the {dinnersize} of you can come right this way")


# import functions

# functions.make_pizza(14, 'peperoni') 
#or you could also do ...

# from functions import make_pizza

# make_pizza(14, 'onions')
# make_pizza(9, 'peppers')

#Using while loops

current_num = 1
while current_num <= 3:
	print(f"\n{current_num}")
	current_num += 1

unconfirmed_users = ['kenny', 'taiwo', 'pluto']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print(f'\nVerifying user: {current_user.title()}')
	confirmed_users.append(current_user)
	# print(confirmed_users)

print("\nThe following users have been confirmed: ")
for users in confirmed_users:
	print(users.title())