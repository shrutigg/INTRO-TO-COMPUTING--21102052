#Question 1
marks = float(input("Enter marks = "))

if marks<25:
    print("Grade : F")
elif marks in range(25,45):
    print("Grade : E")
elif marks in range(45,50):
    print("Grade : D")
elif marks in range(50,60):
    print("Grade : C")
elif marks in range(60,80):
    print("Grade : B")
else :
    print("Grade : A")
    
#-------------------------------------------------------------------------------------------------
    
#Question 2
year = int(input("Enter the year = "))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print(year,"is a Leap year")
        else:
            print(year,"is not a Leap year")
    else:
        print(year,"is a Leap year")
else:
    print(year,"is not a Leap year")
    
#-------------------------------------------------------------------------------------------------    
    
#Question 3
from random import randint, random

for i in range(1,11):
    a = randint(0,9)
    b = randint(0,9)
    answer = a*b

    print("Question ", i,":",a,"x",b,"=")
    ans = int(input())
    if ans==answer:
        print("Right!")
    else:
        print("Wrong. The answer is",answer)
        
#-------------------------------------------------------------------------------------------------
        
#Question 4
for candies in range(200):
    if candies % 5 == 2:
        if candies % 6 == 3:
            if candies % 7 == 2:
                print(candies,'candies are in the bowl!')
© 2022 GitHub, Inc.
Terms
Privacy
Security
