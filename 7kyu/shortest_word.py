def find_short(s):
    text = s.split()
    l = int()
    
    for s in text:
        if l == 0:
            l = len(s)
        elif (len(s) < l):
            l = len(s)
    return l # l: shortest word length