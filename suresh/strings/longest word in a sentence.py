


a=input("enter the element")
b=a.split()
c=""
for i in b:
    if len(i)>len(c):
        c=i
print("the longest word is ",c,"and the length is",len(c))

'''
method 2: usiong the function

def longest_word(sen):
    a=sen.split()
    b=""
    for i in a:
        if len(i)>len(b):
            c=i
    return c,len(c)

sen=input("enter the element")
i,length=longest_word(sen)
print(f"the longest word is {i} and length is {length}")
   '''     

