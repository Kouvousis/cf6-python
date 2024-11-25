def fibonacci(n):
    if n == 0:
        return 0 
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

def main():
    n = int(input("Please insert an int: ")) 
    print(f"The {n}th of Fibo is: {fibonacci(n)}")

if __name__ == "__main__":
    main()