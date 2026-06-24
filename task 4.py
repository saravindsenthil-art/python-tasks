#task 1
'''text=str(input("Enter a word:"))
b=str(input("Enter character to count:"))
print(text.count(b))'''

#task 2
'''text=str(input("Enter a word:"))
vowel=["a","e","i","o","u"]
count=0
for i in text:
    if i in vowel:
        print(i,end=" ")
    count+=1
print("Number of vowels:",count)'''

#task 3
'''text=str(input("Enter a phrase:"))
a=text.split()
for i in a:
    print(i.upper())'''

#task 4
'''text=str(input("Enter a phrase:"))
print(text[ : :-1])'''

#task 5
'''text=str(input("Enter a phrase:"))
a=text.split()
for i in a:
    for b in a:
        if len(i)>len(b):
            b=i
print("The longest word in the above sentence is:",b)'''

#task 6
'''a=str(input("Enter a word:"))
b=a[ : :-1]
if a==b:
    print("The given word is a palindrome")
else:
    print("The given word is not a palindrome")'''
