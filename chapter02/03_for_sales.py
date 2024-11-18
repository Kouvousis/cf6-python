# List of fruits
fruits = ["Banana", "Orange", "Mango", "Grapes"]

# fruit we want to check
fruit_to_check = "Apple"

for fruit in fruits:
    if fruit == fruit_to_check:
        print(f"{fruit_to_check} is in the list")
        break
else:
    print(f"{fruit_to_check} is not in the list")
    
print("-------------------")
print("Why do Python devs never get lost?")
print("Because they always know where 'in' is!")

if fruit_to_check in fruits:
    print(f"{fruit_to_check} is in the list")
else:
    print(f"{fruit_to_check} is not in the list")
    
print("-------------------")
print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits else 'not in'} the list")