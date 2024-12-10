from store import Inventory, Item, OutOfStockError  # from store import *

def main():
    inventory = Inventory()
    
    inventory.add_item(Item("Apple", 10))
    inventory.add_item(Item("Banana", 5))
    inventory.add_item(Item("Apple", 5))    
    
    print("Current inventory")
    inventory.print_items()
    
    print("remove an Apple")
    inventory.remove_item("Apple")
    print("Inventory after removing an apple")
    inventory.print_items()
    
    try:
        inventory.remove_item("Orange")
    except ValueError as e:
        print(e)
        
    try:
        for _ in range(7):
            inventory.remove_item("Banana")
    except OutOfStockError as e:
        print(e)    

if __name__ == "__main__":
    main()