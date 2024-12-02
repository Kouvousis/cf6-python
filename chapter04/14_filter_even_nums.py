numbers = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10] # [i for i in range(1, 11)]

# even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

even_numbers2 = filter(lambda x: x % 2 == 0, numbers)
print(even_numbers2)

print("-----------------------")
for num in even_numbers2:
    print(num, end=" ")
print()

print("-----------------------")
for num in even_numbers2:
    print(num, end=" ")
print()

# use it again and again
even_numbers_list = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers_list)
print(even_numbers_list)
