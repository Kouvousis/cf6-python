def my_avg(*args):
    # if not args:
    #     return 0
    # return sum(args) / len(args)
    return sum(args) / len(args) if args else 0

def main():
    my_ints = [15, 10, 5]
    print(f"Average of my_ints {my_avg(*my_ints)}")
    print(f"Average of 5, 10, 15 {my_avg(5, 10, 15)}")
    print(f"Average of no numbers: {my_avg()}")
    

if __name__ == "__main__":
    main()