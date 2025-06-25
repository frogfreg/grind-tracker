from collections import deque


def updateMatrix(mat):
    finalMat = [[-1] * len(mat[0]) for _ in range(len(mat))]

    q = deque()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                finalMat[i][j] = 0
                q.append((i, j))

    while q:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        tup = q.popleft()

        for d in directions:
            newRow = tup[0] + d[0]
            newCol = tup[1] + d[1]

            if (
                0 <= newRow < len(mat)
                and 0 <= newCol < len(mat[0])
                and finalMat[newRow][newCol] == -1
            ):
                q.append((newRow, newCol))
                finalMat[newRow][newCol] = 1 + finalMat[tup[0]][tup[1]]

    return finalMat
