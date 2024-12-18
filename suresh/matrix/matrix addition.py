r=int(input("enter the no of rows: "))
c=int(input("enter the no of columns: "))

m1=[]
m2=[]

print("enter the elements into the m1 matrix")
for i in range(r):
    m1.append([int(input(f"enter the element m1[{i}{j}] :"))for j in range(c)])
print("enter the elements into the m1 matrix")
for i in range(r):
    m2.append([int(input(f"enter the element m2[{i}{j}] :"))for j in range(c)])

result=[[m1[i][j]+m2[i][j] for j in range(c)]for i in range(r)]

print("addition of matrix")
for row in result:
    print(row)

