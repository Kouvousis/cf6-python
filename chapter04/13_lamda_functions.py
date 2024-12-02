# lambda expressions
# Example power of a number.
# Parameters: 
# base (int): The base number to be raised to power
# exp (int): The exponent indication the power to witch the base is raised. 
# Returns
# The results of raising the 'base' to power of 'exp' (base ^ exp) ---> base ** power
def my_pow(base, exp):
    return base ** exp

power_to = lambda base, exp: base ** exp

def main():
    print(my_pow(2, 2))
    print(power_to(2, 2))
    
if __name__ == "__main__":
    main()