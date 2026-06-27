#task 1
'''def listing():
    for i in range (1,51):
        print(i)'''

#task 2
'''def addition(a,b):
    print(a+b)'''
#task 3
'''def opperation():
    a=[1,3,5,7,9]
    total=0
    for i in a:
        total+=i
    print("total:",total)
    print("Average:",total/len(a))
    for i in a:
        for b in a:
            if b>i:
                i==b
    print("Max",i)
opperation()'''

#task 4
'''def maximum(a,b,c):
    if a>b and a>c:
        return a
    else:
        if b>c:
            return b
        else:
            return c

k=maximum(2,4,5)
print(k)'''

#task 5
'''def stu_details(name,age,height,weight):
    print("name:",name)
    print("age:",age)
    print("height:",height)
    print("weight:",weight)
stu_details("Auravind",17,186,52)'''

#task 6
'''def area(length,breath):
    area=length*breath
    print("area:",area)
area(25,34)'''

#task 7
'''def interest(loan,interest_rate):
    interest=loan*(interest_rate/100)
    print("interest:",interest)
interest(60,2)'''

#task 8
'''def exp(base,exponent=2):
    exp=base**exponent
    print("exp:",exp)
exp(5)
'''

#task 9
'''def add(*add):
    sum=0
    for i in add:
        sum+=i
    print("sum:",sum)
add(12,345,21,1)'''

#task 10(incomplete)
'''def maxi(*maxi):
    largest=0
    for i in maxi:
        if i>largest:
            largest=i
    print("largest:",largest)
maxi(12,345,21,1)'''



#task 11
'''def display(**display):
    for i in display:
        print(i,display[i])
display(name="erty",age=22,height=23,weight=24)'''

#task 12
'''def display(**display):
    for i in display:
        print(i,display[i])



display(name="erty",age=22,height=23,weight=24)'''

#task 13
'''c=lambda a:(a**2)
print(c(int(input("enter your number:"))))'''

#task 14
''''c=lambda a,b:a if a>b else b
print(c(int(input("enter your number:")),int(input("enter your number:")))'''

#task 15
'''temp_in_c=[15,30,37,100]
temp_in_f=list(map(lambda x:x*1.8,temp_in_c))
print(temp_in_f)'''

#task 16
'''p=[2,4,6,8,7]
square=list(map(lambda x:x**2,p))
print(square)'''

#task 17
'''p=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda x:x%2==0,p))
print(even)'''

#task 18
'''p=[1,10,234,345678,5,567]
q=list(filter(lambda x:x>100,p))
print(q)'''

#task 19
'''def power(a,b):
    if b==1:
        return a
    else:
        return a*power(a,b-1)


k=power(3,4)
print(k)'''

#task 20
'''def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
k=fibonacci(6)
print(k)'''









