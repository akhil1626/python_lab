class rectangle:
    
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def length(self):
        return self.length
    def breadth(self):
        return self.breadth
    def isSquare(self):
        if(self.length==self.breadth):
            return True
        else:
            return False
r1=rectangle(2,2)
print(r1.area())
print(r1.perimeter())
print(r1.isSquare())
r2=rectangle(4,2)
print(r2.area())
print(r2.perimeter())
print(r2.isSquare())
    
        