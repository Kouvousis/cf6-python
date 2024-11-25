def is_armstrong_number(n):
    digits = str(n)
    power = len(digits)
    total = 0
    
    for digit in digits:
        total += int(digit) ** power
    
    return n == total

def main():
    try:
        num = int(input("Please insert an integer:"))
    except ValueError:
        print("Invalid number")
        return
    
    if is_armstrong_number(num):
        print(f"{num} is an armstrong number")
    else:
        print(f"{num} is not an armstrong number")
        
        

if __name__ == "__main__":
    main()