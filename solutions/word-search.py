def wordInBoard(board, word):
    visited = set()
    rows, cols = len(board), len(board[0])

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0]:
                visited.add((i, j))
                if searchWord(board, visited, (i, j), word[1:]):
                    return True
                visited.remove((i, j))

    return False


def searchWord(board, visited, rowAndCol, word):
    if len(word) == 0:
        return True

    r = rowAndCol[0]
    c = rowAndCol[1]

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    neighbors = []
    for d in directions:
        newRow = r + d[0]
        newCol = c + d[1]
        if (
            0 <= newRow < len(board)
            and 0 <= newCol < len(board[0])
            and board[newRow][newCol] == word[0]
            and (newRow, newCol) not in visited
        ):
            neighbors.append((newRow, newCol))

    for n in neighbors:
        row, col = n[0], n[1]

        visited.add((row, col))
        if searchWord(board, visited, (row, col), word[1:]):
            return True

        visited.remove((row, col))

    return False
