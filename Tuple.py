# 3.1 Create and access
my_tuple = (10, 20, 30)
print("Tuple:", my_tuple)
print("Access element at index 1:", my_tuple[1])

# 3.2 Nested Tuple
nested_tuple = (1, 2, (3, 4), 5)
print("Nested Tuple:", nested_tuple)
print("Access nested element:", nested_tuple[2][1])

# 3.3 Repetition of tuple
repeated = my_tuple * 2
print("Repeated Tuple:", repeated)

# 3.4 Concatenation of tuples 
my_tuple2 = (40, 50, 60)
result = my_tuple1 + my_tuple2
print(result) 
