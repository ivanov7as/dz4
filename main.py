def martix_transpond(matrix):
    transpond = []
    n = len(matrix)
    m = len(matrix[0])
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(matrix[j][i])
        transpond.append(temp)

    print(transpond)


martix_transpond([[1, 2, 3], [4, 5, 6]])
