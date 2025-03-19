from functions import make_pizza

print("Press 'q' at any time to quit this program !")

while True:
	size = input("\nTell us what size of pizza you would like : ")
	if size == 'q':
		break
	toppings = input("\nWhat topping would you prefer : ")
	if size == 'q':
		break

	my_pizza_test = make_pizza()
	print(f"\nI love a {my_pizza_test}\n")