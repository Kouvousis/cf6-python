def calculator(num1, num2, operation):
    try:
        return operation(num1, num2)
    except TypeError as e:
        print(f"Error: {e}. Ensure the 'operation' argument is a function taking two arguments.")
        return None

def add(n1 , n2):
    return n1 + n2
    
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Division by 0 is not allowed.")
    return n1 / n2

def main():
    print("Addition:", calculator(5, 3, add))
    print("Subtraction:", calculator(10, 7, subtract))
    print("Multiplication:", calculator(5, 3, multiply))
    print("Division:", calculator(10, 5, divide))

if __name__ == "__main__":
    main()