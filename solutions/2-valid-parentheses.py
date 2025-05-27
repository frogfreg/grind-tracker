def isValid(s):
    parens = {"(": ")", "[": "]", "{": "}"}
    stack = []

    for char in s:
        if char in parens:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False

            lastElem = stack.pop()
            if parens[lastElem] != char:
                return False

    return len(stack) == 0
