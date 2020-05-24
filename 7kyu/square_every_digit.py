def square_digits(num):
    
    int_string = ''
    
    for i in str(num):
        int_string += str(int(i) ** 2)

    return int(int_string)