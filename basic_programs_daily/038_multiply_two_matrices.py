# Write a Python Program to Multiply Two Matrices.


def multiply_matrices(mat1, mat2):
    # determine the dimensions of the input matrices
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])

    if cols1 != rows2:
        return "Matrix multiplication is not possible."

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result


matrix1 = [[1, 2, 3], [4, 5, 6]]

matrix2 = [[7, 8], [9, 10], [11, 12]]

result_matrix = multiply_matrices(matrix1, matrix2)

# display the result

if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Result of matrix multiplication:")
    for row in result_matrix:
        print(row)
