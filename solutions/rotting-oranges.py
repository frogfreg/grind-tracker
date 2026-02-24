from collections import deque


def orangesRotting(grid: list[list[int]]) -> int:
    queue = deque([])
    visited = set()
    minutes = 0
    healthy = []

    for ri in range(len(grid)):
        for ci in range(len(grid[0])):
            if grid[ri][ci] == 2:
                queue.append((ri, ci, 0))
            elif grid[ri][ci] == 1:
                healthy.append((ri, ci))

    while queue:
        curr = queue.popleft()
        if (curr[0], curr[1]) in visited:
            continue
        visited.add((curr[0], curr[1]))
        minutes = max(minutes, curr[2])
        neighbors = getNeighbors(curr[0], curr[1], len(grid), len(grid[0]))

        for n in neighbors:
            if n not in visited and grid[n[0]][n[1]] == 1:
                queue.append((n[0], n[1], curr[2] + 1))

    for pair in healthy:
        if pair not in visited:
            return -1

    return minutes


def getNeighbors(ri, ci, lenRows, lenCols):
    directions = ([0, 1], [1, 0], [0, -1], [-1, 0])

    neighbors = []

    for d in directions:
        if 0 <= ri + d[0] < lenRows and 0 <= ci + d[1] < lenCols:
            neighbors.append((ri + d[0], ci + d[1]))

    return neighbors

