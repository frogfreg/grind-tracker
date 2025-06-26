from collections import deque


def numIslands(grid):
    visited = set()
    landQueue = deque()
    count = 0

    for rIndex in range(len(grid)):
        for cIndex in range(len(grid[0])):
            if grid[rIndex][cIndex] == "1":
                landQueue.append((rIndex, cIndex))

    while landQueue:
        row, col = landQueue.popleft()

        if (row, col) in visited:
            continue

        neighbors = deque()
        neighbors.append((row, col))
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while neighbors:
            tup = neighbors.popleft()
            curRow = tup[0]
            curCol = tup[1]

            if (curRow, curCol) in visited:
                continue

            visited.add((curRow, curCol))

            for d in directions:
                newRow, newCol = curRow + d[0], curCol + d[1]

                if (
                    0 <= newRow < len(grid)
                    and 0 <= newCol < len(grid[0])
                    and (newRow, newCol) not in visited
                    and grid[newRow][newCol] == "1"
                ):
                    neighbors.append((newRow, newCol))

        count += 1

    return count
