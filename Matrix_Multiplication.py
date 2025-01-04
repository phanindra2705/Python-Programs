# Matrix Multiplication
def matrix_multiplication(A, B):
    result = [[sum(x * y for x, y in zip(row, col)) for col in zip(*B)] for row in A]
    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

result = matrix_multiplication(matrix1, matrix2)
for row in result:
    print(row)
