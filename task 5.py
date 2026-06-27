 #List tasks
#1
'''x=["tim","top","bip","bop","bob"]
print(x.append("bib"))
print(x)
print(x.remove("top"))
print(x)'''

#2(incomplete)
'''a=[10,20,30,50,40]
b=0
for i in a:
    
        if i>b:
            b=i
print("The largest number in the list is:",b)
b=0
for i in a:
    
        if i<b:
            b=i
print("The smallest number in the list is:",b)'''

#3
'''a=[1,2,3,4,5,6,7]
count=0
for i in a:
    if i%2==0:
        count+=1
print("The number of even is:",count)
count_odd=0
for i in a:
    if i%2==1:
        count_odd+=1
print("The number of odd is:",count_odd)'''

#4
'''a=[1,2,3,4,5,6,7]
print(a.reverse())
print(a)'''

#5
'''a=[67,9,450,21,10001]
print(a.sort())
print(a)'''

#6
'''a=[67,9,450,21,10001]
total=0
for i in a:
    total+=i
print("The sum of elements of the list is:",total)
print("The average of elements of list is:",total/len(a))'''

#7(incomplete)

#tuple
'''a=(1,2,3,4,5,1)
print(a.index(3))
print(len(a))
print(a.count(1))
x=list(a)
print(x[0:2])
y=tuple(x)
print(y)

'''
#set
'''a={1,2,3,4,5,1}
b={2,4,6,8,2}

print(a.add(7))
print(a)
print(a.remove(2))
print(a)
print(a|b)
print(a&b)
print(a-b)
c=[1,2,3,3,4]
d=set(c)
print(d)'''

'''print(a.issubset(b))
print(b.issuperset(a))'''

'''vowels=["a","e","i","o","u"]
s=str(input("Enter a string"))
found=set()
for i in s.lower():
    if i in vowels:
        found.add(i)
print(found)'''

#dictionary
'''stu_det={"name":"Aravind","class":"12","gender":"male"}

stu_det.update({"blood_group":"B+ve"})
print(stu_det)
stu_det.update({"class":"grad"})
print(stu_det)
stu_det.pop("class")
print(stu_det)
print(stu_det.keys())'''
         


      
        
        
