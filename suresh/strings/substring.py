def substring(a,b):
    i=a.find(b)
    if i!=-1:
        print(f"The substring start at index : {i}")
    else:
        print("there is no substring present in the string")

a=input("enter the main string")
b=input("enter the sub string")
substring(a,b)f
