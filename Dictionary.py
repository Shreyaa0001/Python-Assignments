#4.1 Create and access dictionary elements
my_dict = {'name': 'Alice', 'age': 25}
print("Dictionary:", my_dict)
print("Access 'name':", my_dict['name'])

# 4.2 Update Dictionary
my_dict['age'] = 26
print("Updated Dictionary:", my_dict)

# 4.3 Removing Elements
del my_dict['name']
print("After removing 'name':", my_dict)

# 4.4 Merging of Dictionaries
my_dict2 = {'gender': 'Female', 'place': 'Cnada'}
my_dict1.update(my_dict2)
print(my_dict1)   


