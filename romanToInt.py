# basic way that i think about it first:
def romanToInt(s: str) -> int:
    totale = 0   
    for i in range(0,len(s)):
        if s[i] == "I":
            totale = totale + 1
        elif s[i] == "V":
            if i > 0 and s[i - 1] == "I":
                totale += 3
            else:
                totale += 5            
        elif s[i] == "X":
            if i > 0 and s[i - 1] == "I":
                totale += 8
            else: 
                totale += 10
        elif s[i] == "L":
            if i > 0 and s[i - 1] == "X":
                totale += 30
            else:
                totale += 50
        elif s[i] == "C":
            if i > 0 and s[i - 1] == "X":
                totale += 80
            else:
                totale += 100
        elif s[i] == "D":
            if i > 0 and s[i - 1] == "C":
                totale += 300
            else:
                totale += 500
        elif s[i] == "M":
            if i > 0 and s[i - 1] == "C":
                totale += 800
            else:
                totale += 1000
    return totale

# after reconize the exercice better: 

def romanToInt(s: str) -> int:
    symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
    totale = 0
    for i in range(len(s)):
        if i + 1 < len(s) and symbol[s[i]] < symbol[s[i + 1]]:
            totale -= symbol[s[i]]
        else:
            totale += symbol[s[i]]
    return totale