def process_characters():
    ch = input("Please insert a char: ")
    
    while ch != "#":
        print(ch, ":", ord(ch))
        ch = input("Please insert a char: ")
        
    print("Goodbye")
    
def process_characters2():
    while True:
        ch = input("Please insert a char: ")
        print(ch, ":", ord(ch))
        if ch == "#":
            break
        
        
    
def main():
    process_characters()

if __name__ == "__main__":
    main()