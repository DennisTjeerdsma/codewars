def xo(s):
    
    count_x = 0
    count_o = 0
    
    for c in s:
        if c.lower() == 'x':
            count_x += 1
        elif c.lower() == 'o':
            count_o += 1
            
    
    return True if count_x == count_o else False