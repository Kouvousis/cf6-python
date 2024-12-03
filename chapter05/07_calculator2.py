import functools

def calculate(args: list[float]) -> dict:
    """
    Generate functions to perform arithmetic operations on a list of numbers.
    
    Parameters:
        args (list of floats): List of numbers to perform operations on.
        
    Returns:
        dict: A dictionary of functions for addition, subtraction, multiplication and average.
        
    """
    def plus() -> float:
        """Returns the sum of numbers in a list."""
        return functools.reduce(lambda x, y: x + y, args)
    
    def minus() -> float:
        """Returns the result of subtraction the numbers in the list"""
        return functools.reduce(lambda x, y: x - y, args)
    
    def mul() -> float:
        """Returns the result of multiplication of the numbers in the list"""
        return functools.reduce(lambda x, y: x * y, args)
    
    def average() -> float:
        """Returns the average of numbers in the list"""
        return sum(args) / len(args)
    
    return {
        "add":plus,
        "subtract":minus,
        "multiply":mul,
        "average":average
    }

def main():
    args = [5, 4, 3, 2, 1]
    operations = calculate(args)
    
    while True:
        print("\nChoose an operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Average")
        print("5. Exit")
        
        try:
            choice = int(input("Enter a choice (1-5): "))
        except ValueError:
            print("Invalid input.")
            
        match choice:
            case 1:
                print("Addition result:", operations['add']())
            case 2:
                print("Subtraction result:", operations['subtract']())
            case 3:
                print("Multiplication result:", operations['multiply']())
            case 4:
                print("Average result:", operations['average']())
            case 5:
                print("Goodbye")
                break
            case _:
                print("Invalid choice")
                        

if __name__ == "__main__":
    main()