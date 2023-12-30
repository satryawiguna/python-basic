class MyFirstClass():
    pi = 3.14

    def __init__(self, radius = 1) -> None:
        self.radius = radius

    def area(self):
        return (self.radius * self.radius) * self.pi # MyFirstClass.radius
    
    def set_radius(self, new_radius):
        self.radius = new_radius
    
x = MyFirstClass(3)
# x.radius = 100
x.set_radius(999)
print(x.area())