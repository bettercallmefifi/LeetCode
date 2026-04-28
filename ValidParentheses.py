def isValid(self, s: str) -> bool:
    overed = ['(', '{', '[']
    fermed = [')', '}', ']']
    i = 0
    thislist = []
    while i < len(s):
        if s[i] in overed:
            thislist.append(s[i])
        elif s[i] in fermed:
            if not thislist:
                return False
            t = thislist.pop()
            if s[i] == ')' and t != '(':
                return False
            if s[i] == '}' and t != '{':
                return False
            if s[i] == ']' and t != '[':
                return False
        i += 1
    return len(thislist) == 0