def canFinish(numCourses, prerequisites):
    dependenceDict = {}

    for courseDependence in prerequisites:
        a, b = courseDependence[0], courseDependence[1]
        if a not in dependenceDict:
            dependenceDict[a] = set([b])
        else:
            dependenceDict[a].add(b)

    doable = set()
    for i in range(numCourses):
        if i not in dependenceDict:
            doable.add(i)

    def canDo(course, seen):
        if course in seen:
            return False

        if course in doable:
            return True

        prevSeen = [c for c in seen]
        prevSeen.append(course)

        for dep in dependenceDict[course]:
            if not canDo(dep, prevSeen):
                return False

            doable.add(dep)

        return True

    for course in dependenceDict:
        if not canDo(course, []):
            return False

    return True
