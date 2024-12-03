list_of_ints = [1, 2, 3, 4, 5, 6, 7]

# use list comprehension to square each number in the list
square_list_compr = [num**2 for num in list_of_ints]

print(square_list_compr)

# use map with a lambda to square the nums of the list
square_list_map = list(map(lambda num: num ** 2, list_of_ints))
print(square_list_map)

def square_function(num):
    return num ** 2

# list compr with named function and if condition
filtered_nums_list = [square_function(num) for num in list_of_ints if num % 2 == 0]
print(filtered_nums_list)

# using map and filtered
filtered_squared_map_filter = list(map(lambda num: num ** 2, filter(lambda num: num % 2 == 0, list_of_ints)))
print(filtered_squared_map_filter)