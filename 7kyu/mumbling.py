def accum(s):
    result = ''
    counter = 0
    
    for c in s:
        if counter > 0:
            result += '-'
        result +=  c.upper() +  counter * c.lower()
        counter += 1
    return result