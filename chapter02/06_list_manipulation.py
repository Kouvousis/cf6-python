fruits = ["Apple", "Banana", "Cherry", "Apple"]
print("Initial list of fruits:", fruits)

# Add
fruits.append("Berry")
print("After adding Berry", fruits)

# Add
fruits.extend(["Berry", 'Fig'])
print("After adding Berry and Grapes and Fig", fruits)

# Insert 1 item in a specific position
fruits.insert(1, "Coconut")
print("After insert Coconut at pos 1", fruits)

# Update Apple to Melon 
fruits[0] = "Melon"
print("After update element at pos 0", fruits)

# Update 2 elements
fruits[1:3] = ["A", "B"]
print("List after update 2 elements:", fruits)

# fruits[0] = [1, 2, 3, 4, 5]
# print(fruits)

#  delete
removed_item = fruits.pop(1)
print(f"Removed item: {removed_item}")
print(fruits)

new_removed_item = fruits.remove("B")   # Does not return value (returns None)
print(f"Removed item: {new_removed_item}")
print(fruits)

# Remove a fantastic item
# fruits.remove("Exotic_Fruit")
# print(fruits)

if new_removed_item in fruits:
    print(f"{new_removed_item}")
else:
    print(f"{new_removed_item} doesn't exists")
    
# Search
pos = fruits.index("Melon")
print(f"In position: {pos} exists {fruits[pos]}")
