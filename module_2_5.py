def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
print(get_matrix(2, 2, 10))  # [[10, 10], [10, 10]]
print(get_matrix(3, 5, 42))  # [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]]
print(get_matrix(4, 2, 13))  # [[13, 13], [13, 13], [13, 13], [13, 13]]
