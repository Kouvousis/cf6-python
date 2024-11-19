class Base:
    def __init__(self, name):
        self.name = name
        

class Derived(Base):
    def __init__(self, name , lastname):
        super().__init__(name)
        self.lastname = lastname
        
def main():
    base = Base("Jim")
    der = Derived("Jim", "Kouvousis")
    
    print(der.name, der.lastname)
    
if __name__ == "__main__":
    main()