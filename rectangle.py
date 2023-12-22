class Rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
    def get_length(self):
        return self.__length
    def get__breadth(self):
        return self.__breadth
    def area(self):
        return self.get_length()*self.get_breadth()
    def __lt__(self,ob):
        if(self.area()<ob.area()):
              return "first rectangle is small"
        else:
              return "second rectangle is small"
l1=int(input("Enter lenght 1: "))
b1=int(input("Enter breadth 1: "))
ar1=Rectangle(l1,b1)
l2=int(input("\nEnter length 2: "))
b2=int(input("Enter breadth 2: "))
ar2=Rectangle(l2,b2)
print("Area of Rectangle 1: ",ar1.area())
print("Area of Rectangle 2: ",ar2.area())
print(ar1<ar2)
