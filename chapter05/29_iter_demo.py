class DataCollection:
    def __init__(self, data):
        self.data = data
    
    def __iter__(self):
        return iter(self.data)
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __repr__(self):
        return f"DataCollection{self.data}"

def main():
    collection = DataCollection([1, 2 , 3, 4, 5])
    
    print(f"collection: {collection}")
    
    print("Iteration")
    for item in collection:
        print(item, end=", ")
    print()
    
    print("Unpacking...")
    a, b, c, d, e = collection
    print(a, b, c, d, e)
    
    print("INdexing")
    print(f"collection[1]: {collection[1]}")
    
    print("Slicing")
    print(f"collection[1:3]: {collection[1:3]}")
    
    print(f"lean(collection): {len(collection)}")

if __name__ =="__main__":
    main()     