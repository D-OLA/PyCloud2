alien_0 = {'color': 'green', 'points': 5, 'speed': 'medium'}

alien_0['x-axis'] = 0
alien_0['y-axis'] = 25

# print(alien_0['y-axis'], alien_0)

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

# print(f'The original x position is :{alien_0['x-axis']}')
# alien_0['x-axis'] = alien_0['x-axis'] + x_increment
# print(f'The new x position is :{alien_0['x-axis']}')


favprolang = {
	'ken': 'java',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

for key, value in favprolang.items():
	print(f"\n{key.title()}'s favorite programming language is {value}")
# print("The following languages were mentioned: \n")

# for language in set(favprolang.values()):
# 	print(language.title())
# print('\n')


#How to check for a key in a dictionary
# print(favprolang.get('jenny', 'No such user.'))

Kentucky = {
	'first_name': 'Okoturo',
	'last_name': 'Mofe',
	'age': 28,
	'city': 'Asaba'
}
# print(Kentucky['first_name'])
# print(Kentucky['last_name'])
# print(Kentucky['age'])
# print(Kentucky['city'])

# for key, value in Kentucky.items():
# 	print(f"\nKey:{key}",f"value:{value}")

users = {
	'alstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
	},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'germany',
	}
}

for ussername, user_info in users.items():
	print(f"\nUsername: {ussername}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")