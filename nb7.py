def scalar_multiply(matrix, scalar):
    result = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j] * scalar

    return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
scalar = 3

result = scalar_multiply(matrix, scalar)

print("Original matrix:")
for row in matrix:
    print(row)

print("\nResult of scalar multiplication:")
for row in result:
    print(row)
