#average of 3 numbers
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
num3 = float(input("enter third number: "))
a=(num1+num2+num3)/3
print("the average of num1,num2 and num3 is:",a)


#area of circle
a=int(input("circle=1, square=2, triangle=3: "))
if a==1 :
    r=float(input("enter the radius of the circle:"))
    ans=(r**2)*3.14
    print(ans,"sqCm is the area of the prespective circle")
elif a==2 :
    l=float(input("enter the length of the square:"))
    b=float(input("enter the width of the square:"))
    ans=l*b
    print(ans,"sqCm is the area of the prespective square")
elif a==3 :
    h=float(input("enter the height of the triangle:"))
    w=float(input("enter the width of the triangle:"))
    ans=h*w*0.5
    print(ans,"sqCm is the area of the prespective triangle")
else :
    print("there is no specific number")

#square root
num1=int(input("enter the number: "))
a=num1**0.5
print("the square root of num1 is:", a)

#last digit
num1=int(input("enter the number: "))
a=num1%10
print("the last digit is:", a)





