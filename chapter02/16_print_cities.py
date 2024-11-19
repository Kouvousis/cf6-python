def print_cities(*cities, separator = ", ", end = "\t"):
    """  # TODO finish doc comments
    
    
    *cities (str): 
    """
    if not cities:
        print("No cities provided")
    else:
        print("Cities:", ", ".join(cities), sep=separator, end=end)

def main():
    print_cities("Athens", "London", "Paris", separator=" | ", end=".")
    # print_cities("Athens")
    # print_cities()
    

if __name__ == "__main__":
    main()