from functools import reduce

# list of numbers
my_ints = [1, 2 ,3, 4, 5]

# return a result: 1 * 2 * 3 * 4 * 5
result = reduce(lambda x, y: x * y, my_ints)
print("Result:", result)

result2 = reduce(lambda x, y: x * y, my_ints, 100)
print("New result:", result2)