from re import S


s="Hellof    World gege    "

def lengthOfLastWord(s: str) -> int:
        p = len(s) - 1
        while p >= 0 and s[p] == ' ':
            p -= 1
        length = 0
        while p >= 0 and s[p] != ' ':
            p -= 1
            length += 1
        print(length)
lengthOfLastWord(s)