def calculate_sum_and_product(upper_bound):
    total_sum = 0
    total_product = 1
    
    for i in range(1, upper_bound + 1):
        total_sum += i
        total_product *= i
    
    return total_sum, total_product

def main():
    try:
        num = int(input("Please insert a positive integer: "))
        if num <= 0:
            raise ValueError
    except ValueError:
        print("Invalid number")
        return
    
    my_sum, my_product = calculate_sum_and_product(upper_bound=num)
    
    # print(f"Sum (1 - {num} = {t[0]})")
    # print(f"Product (1 - {num} = {t[1]})")
    
    print(f"Sum (1 - {num} = {my_sum})")
    print(f"Product (1 - {num} = {my_product})")
    
                
if __name__ == "__main__":
    main()