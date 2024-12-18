def multiply(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            total = 0                                                                   
            for k in range(len(a[0])):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)
     return result

def get_matrix_input(r, c):
    mat = []
    for i in range(r):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        mat.append(row)
    return mat

rows_a = int(input("Enter the number of rows for matrix A: "))
cols_a = int(input("Enter the number of columns for matrix A: "))
a = get_matrix_input(rows_a, cols_a)

rows_b = int(input("Enter the number of rows for matrix B: "))
cols_b = int(input("Enter the number of columns for matrix B: "))
b = get_matrix_input(rows_b, cols_b)

if cols_a != rows_b:
    print("We cannot multiply these matrices due to incompatible dimensions.")
else:
    result = multiply(a, b)
    print("Resultant matrix:")
    for row in result:
        print(row)
