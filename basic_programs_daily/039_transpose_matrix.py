# Write a Python Program to Transpose a Matrix.


def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    # create an empty matrix to store the transposed data
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


# test matrix
matrix = [[1, 2, 3], [4, 5, 6]]

# transpose the matrix
transposed_matrix = transpose_matrix(matrix)

# print the transposed matrix
for row in transposed_matrix:
    print(row)
