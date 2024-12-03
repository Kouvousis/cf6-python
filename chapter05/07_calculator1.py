from functools import reduce

def calculate(args):
    def plus():
        return reduce(lambda x, y: x + y, args)
    
    def minus():
        return reduce(lambda x, y: x - y, args, 0)
    
    def mul():
        return reduce(lambda x, y: x * y, args)
    
    def div():
        # alternative scenario: if not 0 in args[1:]
        if sum(args[1:]) != 0:
            return args[0] / sum(args[1:])
    
    return plus, minus, mul, div

def main():
    ints_list = [26, 1, 2, 3, 4, 5]
    add_func, minus_func, mul_func, div_func = calculate(ints_list)
    print("add_func:", add_func())
    print("minus_func:", minus_func())
    print("mul_func:", mul_func())
    print("div_func:", div_func())
    

if __name__ == "__main__":
    main()