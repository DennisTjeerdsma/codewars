def get_sum(a,b):

    if b < a:
        a, b = b, a
        
    print(f"a == {a}, b == {b}")
    result = 0
    for i in range(a, b+1):
        result += i
        
    return result