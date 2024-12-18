def nonrepeat(s):
    for char in s:
        if s.count(char)==1:
            return char

s=input("enter string")
res=nonrepeat(s)

if res:
    print(f"the first non repeating character : {res}")
else:
    print("no non repeat characters was found")
  
