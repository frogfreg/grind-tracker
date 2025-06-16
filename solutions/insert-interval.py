def insert(intervals, newInterval):
    leftInter = []
    rightInter = []
    left = newInterval[0]
    right = newInterval[1]

    for inter in intervals:
        if inter[1] < newInterval[0]:
            leftInter.append(inter)
        elif inter[0] > newInterval[1]:
            rightInter.append(inter)
        else:
            left = min(left, inter[0])
            right = max(right, inter[1])

    return leftInter + [[left, right]] + rightInter
