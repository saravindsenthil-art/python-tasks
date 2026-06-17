#task 1
'''a=int(input("enter a value:"))
b=a&1
if b==1:
    print("the given value is odd")
elif b!=1:
    print("the given value is even")'''

#task 2
'''a=int(input("enter a value:"))
if a<0:
    print("the value is negative")
elif a>0:
    print("the value is positive")
else:
    print("the value is 0")'''

#task 3
'''a=int(input("enter a value:"))
b=a%10
if b==0:
    print("the given number is divisible by both 2 and 5")
else:
    print("the given number is not divisible by 2 and 5 at the same time")'''

#task 4
'''marks=int(input("enter your marks:"))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=30:
    print("Grade D")
else:
    print("Grade F")'''

#task 5
'''a=int(input("enter a year:"))
b=a%4
c=a%100
d=a%400
if b==0:
    if d==0:
        print("The given year is a leap year")
    elif c==0:
        print("the given year is not a leap year")
    elif b==0:
        print("the given year  is a leap year")
else:
    print("The given year  is not a leap year")'''

#task 6
'''for i in range(1,11):
    print(i)'''

#task 7
'''for i in range(1,11):
    print("Square of",i,"is",i**2)'''

#task 8
'''for i in range(10,0,-1):
    print(i)'''

#task 9
'''a=int(input("enter your age:"))
if a in range(0,13):
    print("You are a child")
if a in range(13,20):
    print("You are a Teen")
if a in range(20,60):
    prnt("You are an adult")
if a in range(60,2**64):
    print("You are a senior")'''

#task 10
'''a=float(input("enter a number:"))
if a**3<=100:
    print("The cube of the given input is less than 100")
else:
    print("The cube of the given input is more than 100")'''

#task 11
#username:aravind,password:aravind67
'''a=input("Enter your username:")
if a=="aravind":
    b=input("enter your password:")
    if b=="aravind67":
        print("Login succesful")
    else:
        print("Login failed,invalid password")
else:
    print("invalid username")'''

#task 12
'''alphabet=input("Enter an alphabet:")
if alphabet in ["a","e","i","o","u"]:
    print("The given alphabet is a vowel")
else:
    print("The given alphabet is a consonant")'''

#task 13
'''n=int(input("Enter a natural number"))
print((n*(n+1))/2)'''

#task 14
'''p=65
for i in range(1,27):
    print(chr(p))
    p+=1
print()'''

#task 15
'''p=9
a=1
for i in range(1,11):
    print("9 x",a,"=",p*a)
    a+=1
print()'''

#task 16
'''n=int(input("enter a value:"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i,n-1):
        print("*",end=" ")
    print()'''

#task 17
'''n=int(input("enter a value:"))
for i in range(n):
    for j in range(i+1):
        print(i,end=" ")
    print()
for i in range(n):
    for j in range(i,n-1):
        print(i,end=" ")
    print()

n=int(input("enter a value:"))
for i in range(n):
    for j in range(i+1):
        print(j,end=" ")
    print()
for i in range(n):
    for j in range(i,n-1):
        print(j,end=" ")
    print()

n=int(input("enter a value:"))
p=0
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    print()'''

#task 18
'''n=int(input("enter a value:"))
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1
    print()
p=65
for i in range(n):
    for j in range(i,n):
        print(chr(p),end=" ")
        p+=1
    print()'''
    
#task 19
'''correct_password="Auravind"
while True:
    password=input("Enter your password:")
    if password==correct_password:
        print("Acess Granted")
        break
    else:
        print("Incorrect Password.Try Again")'''

#task 20
'''sum=0
for i in range(1,101):
    sum+=i
print("Final sum:",sum)'''
    
    
