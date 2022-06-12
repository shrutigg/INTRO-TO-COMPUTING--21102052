print("Question 1 \n")
a=int(input("enter number:"))
convert=bin(a)
print(convert)
print("\n")

print("Question 2 \n")
a=str(input("enter expression:"))
print("Ans", eval(a))
print("\n")

print("Question 3 \n")
import math

print((3+4)*5)                                                             #A


n = float(input("Enter the value of n= "))                                 #B
print((n*(n-1))/2)


r = float(input("Enter the value of r= "))                                 #C
print(4*math.pi*r**2)


a = int(input("Enter the value of a = "))                                  #D
b = int(input("Enter the value of b = "))
r = int(input("Enter the value of r = "))

x = math.radians(a)
y = math.radians(b)

print(math.sqrt((r*(math.cos(a))**2) + r*(math.sin(b))**2))


y1 = int(input("Enter the value of y1 = "))                                #E
y2 = int(input("Enter the value of y2 = "))
x1 = int(input("Enter the value of x1 = "))
x2 = int(input("Enter the value of x2 = "))

print((y2-y1)/(x2-x1))
print("\n")

print("Question 4 \n")
for i in range(5):                                                 #A
    print(i)


for i in range(3,10):                                              #B
    print(i)


for i in range(4,13,3):                                            #C
    print(i)


for i in range(15,5,-2):                                           #D
    print(i)


for i in range(5,3):                                               #E
    print(i)
print("\n")

print("Question 5 \n")
h = 1.00794
c = 12.0107
o = 15.9994

h_ = int(input("Enter the number of Hydrogen atoms = "))
c_ = int(input("Enter the number of Carbon atoms = "))
o_ = int(input("Enter the number of Oxygen atoms = "))

mw = (h*h_) + (c*c_) + (o*o_)

print("Molecular Weight of the compound = ", mw)
