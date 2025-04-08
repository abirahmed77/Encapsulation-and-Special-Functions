class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
p1 = Point(2, 3)
p2 = Point(5, 8)

print(p1)
print(p2)