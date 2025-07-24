def letterCombs(digits):
    letters = "abcdefghijklmnopqrstuv"
    nums = "2345678"

    mappings = {}
    idx = 0
    for n in nums:
        if n == "7":
            mappings["7"] = ["p", "q", "r", "s"]
            idx += 4
            continue
        mappings[n] = [letters[idx + i] for i in range(3)]
        idx += 3

    mappings["9"] = ["w", "x", "y", "z"]
    mappings["7"] = ["p", "q", "r", "s"]

    if len(digits) < 1:
        return []

    res = []

    allCombs(res, mappings, "", digits, 0)

    return res


def allCombs(combinations, mappings, currString, digits, digitIndex):
    if digitIndex >= len(digits):
        combinations.append(currString)
        return

    for m in mappings[digits[digitIndex]]:
        allCombs(combinations, mappings, currString + m, digits, digitIndex + 1)
