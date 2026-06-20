def isHappy(self, n: int, seen=None) -> bool:
    if seen is None:
        seen = set()
    p = str(n)
    thislist = []
    for i in p:
        thislist.append(i)
    p = sum(pow(int(i), 2) for i in thislist)

    if p in seen:
        return False
    elif p == 1:
        return True
    else:
        seen.add(p)
        return self.isHappy(p, seen)
