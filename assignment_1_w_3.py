#using encapsulation in class
# class Counter:
#      def __init__(self):
#          self.current = 0

#      def increment(self):
#          self.current += 1

#      def value(self):
#          return self.current

#      def reset(self):
#          self.current = 0
# counter= Counter()
# counter.increment()
# counter.increment()
# counter.increment()
# print(counter.value())

# inheritance  concept in python programming

class Polygon:
     def __init__(self, no_of_sides):
         self.n=no_of_sides
         self.side=[0 for i in range(self.n)]
    #  def inputSides(self):
    #      self.sides=[float(input("Enter side" + str(i+1)+":")) for i in range(self.n)]
         return self.side
     def dispSides(self):
        for i in range(self.n):
            print("sides", i+1, "is",self.sides[i])

# child class
class Triangle(Polygon):
     def __init__(self, no_of_sides):
        Polygon._init_(self,3)
     def findArea(self):
        a,b,c=self.sides
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print("the area of the triangle is %0.2f" %area)


