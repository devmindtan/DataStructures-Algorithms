def sortedMatrix(N, Mat):
    x = []
    for i in range(N):
        for j in range(N):
            x.append(Mat[i][j])

    x.sort()
    k = 0
    for i in range(N):
        for j in range(N):
            Mat[i][j] = x[k]
            k += 1
    return Mat


N = 4
Mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]
print(sortedMatrix(N, Mat))
