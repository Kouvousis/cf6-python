def my_add(*args: int) -> int:
    """
    Calculate the sum of an arbitrary number of integers.
    
    Params:
        *args (int): A variable-length argument of integers.
        
    Returns:
        int: The sum of provided integers.
    """
    return sum(args)

def my_average(*args: int) -> float:
    """
    Calculate the average of an arbitrary numbers of integers.
    
    Params:
        *args (int): A variable-length argument list of integers.
        
    Returns:
        float: The average of the provided integers. Returns 0 if no arguments are provided to avoid division by 0.
    """
    if not args:
        return 0
    return sum(args) / len(args)

def main():
    ages = [27, 35, 38, 18, 22, 26]
    
    print("Average age:", my_average(*ages))

if __name__ == "__main__":
    main()