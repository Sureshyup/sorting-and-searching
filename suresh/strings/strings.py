'''
method 1:

def suresh(a,b):
    a=a.replace(" ","").lower()
    b=b.replace(" ","").lower()

    return sorted(a)==sorted(b)

a=input("enter the first element")
b=input("enter the second element")


if suresh(a,b):
    print("strings are anagram")
else:
    print("strings are not anagram")

method 2:'''

def suresh(s1,s2):

    if(sorted(s1)==sorted(s2)):
        print("strings are anagrams")
    else:
        print("strings are not anagrams")

s1=input("enter the first element")
s2=input("enter the second element")
suresh(s1,s2)

