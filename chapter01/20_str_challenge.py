str = "factory"

for i in range(len(str)):
    print(str[i] * (i + 1))
    
for i in range(len(str)):
    print(str[i] * (i + 1), end="*" * (len(str) -1 - i))
    print()