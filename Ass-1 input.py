#QUES1

a=int(input("enter first number :"))
b=int(input("enter second number  :"))
c=int(input("enter third number :"))
avg=(a+b+c)/3
print(avg)


#QUES2

print("All values are to be entered in dollars")
gross_income = float(input("enter your gross income :"))
dependents = int(input("enter number of dependent :"))

std_deduction = 10000
dep_deduction = 3000
tax_rate = 0.2

taxable_income = (gross_income - std_deduction - (dependents*dep_deduction))
tax = taxable_income*tax_rate

print("taxable income",taxable_income)
print("your tax comes out to be", tax)

#QUES3

print("student = [sid, name, gender, course, cgpa]")
sid = int(input("enter your sid :"))
name = str(input("enter your name :"))
gender = str(input("gender (M,F,U) :"))
course = str(input("course name :"))
cgpa = float(input("enter your cgpa :"))
student = [sid, name, gender, course, cgpa]
print("student info :", student)

#QUES4

a = int(input("enter marks of student 1 :"))
b = int(input("enter marks of student 2 :"))
c = int(input("enter marks of student 3 :"))
d = int(input("enter marks of student 4 :"))
e = int(input("enter marks of student 5 :"))
marks = [a, b, c, d, e]
print("marks of the 5 students are :", marks)

#sorting the list in ascending and descending order

asc = marks.sort()
print("marks in ascending order :", marks)
desc = marks.sort(reverse = True)
print("marks in decsending order :", marks)

#QUES5

list=['red', 'green', 'white', 'black', 'pink', 'yellow']

list.remove("black")
print(list)
list[3]=("purple")
print(list)
