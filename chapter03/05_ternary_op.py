def compare_integers(a, b):
    if a == b:
        print("Equals")
    elif a > b:
        print("First num is greater than second num")
    else:
        print("First num is less than second num")
        
def main():
    try:
        a = int(input("Give me the first integer "))
        b = int(input("Give me the second integer "))
    except ValueError:
        print("Invalid input. PLease give integers.")
        return
    
    compare_integers(a, b)
    
    # 1. Ternary Operator (Simple example)
    result = "Positive" if a > 0 else "Non-Positive"
    print(result)
    
    # 2. Ternary Operator (Extended Example)
    res = (
        "Equals" if a == b else
        "First num is greater than second num" if a > b else
        "First num is less than second num"
        
    )
        

if __name__ == "__main__":
    main()