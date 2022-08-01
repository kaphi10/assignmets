# python program to print exponential of a number
print("CALCULATING EXPONENTIAL OF NUMBER")
a=int(input("Enter the first integer"))
b=int(input("Enter the second integer"))
if b==0:
    print(1)
else:
   for i in range(1,b+1):
    x=a**i
    print(x)