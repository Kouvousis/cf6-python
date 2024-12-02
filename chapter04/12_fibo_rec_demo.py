def fibonacci(n):
    # Base cases: fibonacci(0) = 0, fibonacci(1) = 1
    if n in (0, 1): return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = int(input("Enter a positive integer to find its fibonacci: "))
    print(f"Fibonacci({n}) = {fibonacci(n)}")


if __name__ == "__main__":
    main()