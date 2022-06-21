#Question 1
string1 = input("Enter the string: ")

print(string1[::-1])



#Question 2
lower_limit = int(input("Enter the lower limit of the range:"))
upper_limit = int(input("Enter the upper limit of the range:"))
dividing_number = int(input("Enter the number to divide:"))

for i in range(lower_limit,upper_limit):
    if i%dividing_number==0:
        print(i)
    else:
        continue
        


#Question 3
import math

a = int(input("Enter the length of side 1:"))
b = int(input("Enter the length of side 2:"))
c = int(input("Enter the length of side 3:"))

if (a+b>c and b+c>a and c+a>b):
    s = (a+b+c)/2
    area =  math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(area)
elif (a+b<=c or b+c<=a or c+a<=b):
    print("Triangle can't be formed!!")


    
#Question 4
n = 5
for i in range(n):
    for j in range(i):
        print("* ", end="")
    print("")

for i in range(n,0,-1):
    for j in range(i):
        print("* ", end="")
    print("")



#Question 5
n = int (input("Enter The Number Of Rows: "))
value = 65

for i in range (0,n+1):
    for j in range (0, i):
        ch = chr(value) 
        print (ch, end=" ")
        value = value + 1

        if (value>90) :
            value=65

    print ()

    
#Question 6
lower_limit = int(input("Enter the lower limit of the range:"))
upper_limit = int(input("Enter the upper limit of the range:"))

for i in range(lower_limit,upper_limit+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)
            

            
#Question 7
for i in range(1,501):
    if (i%7 == 0) and (i%11 == 0):
        print(i)
    else:
        continue
        

        
#Question 8
numbers = (input("Enter the list of numbers seperated by comma(,):"))

user_list = list(map(int,numbers.split(",")))

positive_list = []
negative_list = []
odd_list = []
even_list = []

for num in user_list:
    if num>0:
        positive_list.append(num)
              
for num in user_list:
    if num<0:
        negative_list.append(num)

for num in user_list:
    if num%2!=0:
        odd_list.append(num)

for num in user_list:
    if num%2==0:
        even_list.append(num)

for num in user_list:
    count=user_list.count(num)
    print (num,'occurs', count," times")

print("List of Positive Numbers: ", positive_list)
print("List of Negative Numbers: ", negative_list)
print("List of Even Numbers: ", even_list)
print("List of Even Numbers: ", odd_list)



#Question 9
user_list = input("Enter the list of words seperated by comma(,):")

word_list = user_list.split(",")

counts = dict()

for word in word_list:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
