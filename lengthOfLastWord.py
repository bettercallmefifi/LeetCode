def lengthOfLastWord(s: str) -> int:
    thislist = []
    p = s.split(" ")
    for i in p:
        if i != '':
            thislist.append(i)
    return len(thislist[len(thislist) - 1])

print(lengthOfLastWord("luffy is still joyboy"))