my_list = [1, 2, "Hello", [3, 4, 5]]

# iterate
print("At the start")
for item in my_list:
    print(f"{item} : {id(item)}")
    
new_list = my_list * 2
print("Duplicated list:", new_list)

# update 1st item
new_list[0] = 100
print("Updated list:", new_list)

# print(new_list[3][0])
new_list[3][0] = 300
print("Updated list:", new_list)

print("At the start")
for item in new_list:
    print(f"{item} : {id(item)}")
