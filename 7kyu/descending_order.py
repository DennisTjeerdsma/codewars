def descending_order(num):
    if num < 0:
        return 0
    else:
        num_arr = [int(i) for i in str(num)]
        num_arr.sort(reverse=True)
        
        num_string = ''
        
        for i in num_arr:
            num_string += str(i)
        
        num = int(num_string)
    return num
        