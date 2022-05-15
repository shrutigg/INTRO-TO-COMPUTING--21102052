print("         QUESTION - 1\n")

istring="python is a case sensitive language"
print("A) length of input string is:",len(istring))

print("B)reversed string:",istring[::-1])

sliced = istring[istring.find('a case'): istring.find('ive')+3]
#found 'ive' in 'sensitive' then added 3 to adjust the index
print('c) Sliced String:', sliced)

print("D)",istring.replace ("a case sensitive","object oriented"))

pString = istring
print('e. The substring \'a\' was found at index = ', end = '')
i = 0
for travel in pString:
    if travel == 'a':
        #this 2nd if statement is to prevent printing of a ',' at the last index
        #we find the index of the last occurence of 'a'
        if i != (len(pString) - pString[::-1].find('a') - 1): 
            print(i, ', ', sep = '', end = '')
        else:
            print(i)
    i += 1

print("F)",istring.replace(" ",""))



print("\n         QUESTION - 2\n")

name = 'Shruti Garg'
sid = 21102052
department = 'civil'
cgpa = 9

print('Hey! %s here!\n\
My SID is %d\n\
I am from %s department and my CGPA is %f'%(name, sid, department, cgpa))



print("\n         QUESTION - 3\n")

a = 56
b = 10
print('a. a&b =', a&b)
print('b. a|b =', a|b)
print('c. a^b =', a^b)
print('d. a << 2 =', a << 2, 'b << 2 =', b << 2)
print('e. a >> 2 =', a >> 2, 'b >> 4 =', b >> 4)



print("\n         QUESTION - 4\n")

input_string = input('Enter your string: ')

index = input_string.find('name')
# Because find() function returns -1 when the substring is not found in the given string
if index == -1:
    print('No')
else:
    print('Yes')




print("\n         QUESTION - 5\n")

sideList = [0, 0, 0]
for i in range(len(sideList)):
    sideList[i] = int(input('Enter side %d: '%(i+1)))
sideList.sort()

# Checking if the sum of the smallest 2 side lengths
# is greater than the largest side is sufficient
result =  sideList[0] + sideList[1] > sideList[2]

if result:
    print('Yes')
else:
    print('No')



print("\n         QUESTION - 6\n")

flips=0
a=int(input("enter number 1:"))
b=int(input("enter number 2:"))

for x in range (a+b):
  t1=a&1
  t2=b&1
  if (t1!=t2):
    flips+=1

  a>>=1
  b>>=1

print(flips)

      
