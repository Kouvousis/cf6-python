# Populate a set
bag = {"eggs", "apples", "bananas", "eggs"}

print("Initial set:", bag)

# Add a new item to the set
bag.add("oranges")
print("After adding oranges:", bag)

# Remove
item_to_remove = "Eggs"
# bag.remove(item_to_remove)
# print("After removing eggs:", bag)

if item_to_remove in bag:
    bag.remove(item_to_remove)
    
# Iterate through the set
for item in bag:
    print(item)

