def floodFill(image, sr, sc, color):
    if image[sr][sc] == color:
        return image

    initialColor = image[sr][sc]

    seen = set()

    stack = [(sr, sc)]

    while stack:
        currTuple = stack.pop()
        image[currTuple[0]][currTuple[1]] = color
        updateStack(image, stack, seen, currTuple, initialColor)

    return image


def updateStack(image, stack, seenSet, currTuple, initialColor):
    increments = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for inc in increments:
        checkRow = currTuple[0] + inc[0]
        checkCol = currTuple[1] + inc[1]
        if (
            checkRow < 0
            or checkRow >= len(image)
            or checkCol < 0
            or checkCol >= len(image[0])
        ):
            continue

        if (checkRow, checkCol) in seenSet:
            continue

        if image[checkRow][checkCol] == initialColor:
            stack.append((checkRow, checkCol))
            seenSet.add((checkRow, checkCol))
