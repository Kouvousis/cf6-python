# Populate list.
my_list = [1, 2, 3, 4, 5]

# Simple unpacking all of the elements.
a , b, c, d, e = my_list

print(f"Unpacked values: a={a}, b={b}, c={c}, d={d}, e={e}")

# Using the _ as placeholder (for unused elements).
a1, _, c1, _, e1 = my_list

print(f"Unpacked values after skipping some values: a={a}, c={c}, e={e}")

# Unpacking the first element, capturing the rest (in a list).
a2, *rest = my_list

print(f"First element: a2={a2}, remaining elements: rest={rest}")

# Unpacking last element, capturing the rest (in a list).
*start, z = my_list

print(f"Last element: z={z}, remaining elements: start={start}")
# Unpacking the first and the last element, the rest are captured in a list.
first, *middle, last = my_list
print(f"The first element: first={first}, middle elements: middle={middle}, Last element: last={last}")

try:
    a , b, c, d, e = my_list
    print(f"Unpacked values: a={a}, b={b}, c={c}, d={d}, e={e}")
except ValueError as ve:
    print("Error", ve)

# Unpacking the first and 2nd element, capturing the rest element sin a list.
a1, b1, *rest = my_list
print(a1, b1, rest)