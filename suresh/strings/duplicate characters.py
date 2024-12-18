'''
method 1: without using function

a=input("enter the word: ")
b=""
for i in a:
    if i not in b:
        b+=i
print(b)

method 2: with using function'''

def duplicate_string(a):
    result=""
    for i in a:
        if i not in result:
            result+=i
    print(result)

a=input("Enter the element")

print("modified string")
res=duplicate_string(a)
