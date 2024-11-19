# Populate a list
ages = [19, 23, 34, 45]
print("Initial list of ages:", ages)

print("\n Iterating with index and value:")
for index, value in enumerate(ages):    # (index, value)
    print(f"Index: {index}, value: {value}")
    
print("\nIterate with enhanced for")
for age in ages:
    print(age, end=" ")
print