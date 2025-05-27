def isPalindrome(s):
    newS = s.lower()
    newS = [letter for letter in newS if letter.isalnum()]
    return newS == newS[::-1]
