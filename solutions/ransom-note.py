from collections import Counter


def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    rnCounter = Counter(ransomNote)
    magCounter = Counter(magazine)

    for letter in rnCounter:
        if rnCounter[letter] > magCounter[letter]:
            return False

    return True
