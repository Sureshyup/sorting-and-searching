def count_frequency(s1):
    d={}
    for i in s1:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print("character frequency: ")
    for i,count in d.items():
        print(f" character : {i} : number of times : {count}")

s1=input("enter the character")
count_frequency(s1)    
            
        
        
