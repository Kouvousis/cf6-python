class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def __eq__(self, other):
        return isinstance(other, Point) and self._x == other._x and self._y == other._y
    
    def __hash__(self):
        return hash((self._x, self._y))
    
    def __str__(self):
        return f"Point({self._x}, {self._y})"
        
def main():
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = Point(1, 2)
    
    point_dict = {
        p1: "Point 1",
        p2: "Point 2",
        p3: "Point 3",
    }
    
    print(hash(p1))
    print(hash(p2))
    print(hash(p3))
    print(p1 == p3)
    
    for key, value in point_dict.items():
        print(f"{key}:{value}")

if __name__ =="__main__":
    main()     