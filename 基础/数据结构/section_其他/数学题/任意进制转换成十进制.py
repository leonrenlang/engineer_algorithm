def process(s):
    res = 0
    for item in s:
        res = res * 26 + ord(item) - ord('A') + 1
    return res