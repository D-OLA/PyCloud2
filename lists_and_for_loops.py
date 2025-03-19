market_list = ['pepper', 'tomato', 'okra', 'milk', 'milo']
# print (market_list[3])
# message = f"\nThe only thing I forgot to get was {market_list[0]}\n"
# print (message)

names = ['Kanu', 'Quadri', 'Shola', 'Tolu', 'Gbemi']
# for nick in names:
# 	print(nick)

# print (names[0])
# print (names[1])
# print (names[2])
# print (names[3])
# print (names[4])

names.append('Chioma')
print(names)
# names.insert(0, 'Tunde')
# print(names)

# del names[-1]
# print(names)

# popped_out = names.pop()
# print(popped_out)

# names.append(popped_out)
# print(names)

# market_list.remove('milo')
# print(f"\n{market_list}")

# names.sort()
# print(f'{names}\n')

market_list.append('chocolate')
# market_list.reverse()
# print(sorted(market_list))
# market_list.reverse()
# print(f'{market_list}\n')

# print(len(names))
# print(len(market_list))

# magicians = ['Dare', 'Chuy', 'Lola']
# for magician in magicians :
# 	print(f"{magician}, that was a great trick.")
# 	print(f"I can't wait to have you back, {magician}.\n")

# pizzas = ['peperoni', 'cheese', 'chicken']
# for pizza in pizzas:
# 	print(f"I love eating {pizza} pizza\n")

# for value in range(1, 6):
# 	print(value)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# squares = []
# for value in range(1,11):
# 	square = value **2
# 	squares.append(square)

# print(squares)
# print("-----------")
# print("-----------")

# for number in range(1, 21):
# 	print(number)
# print("-----------")
# print("-----------")

million_list = range(1,1000001)
print(min(million_list))
print(max(million_list))

output = sum(million_list)
print(output)

# number_list = range(1,11)
# cube_list = []
# for n in number_list:
# 	cube = n**3
# 	cube_list.append(cube);
# print(cube_list);

# sly = cube_list[0:3];
# for jeets in sly:
# 	print(f"The first slice starting from 0 excluding 3 giving us {sly}\n");

# # Slice operation can also be used to copy over lists

# gpa_list = sly[:]
# print(gpa_list);

# measurments = (23, 56, 98); #This is a Tuple(unchangable list)