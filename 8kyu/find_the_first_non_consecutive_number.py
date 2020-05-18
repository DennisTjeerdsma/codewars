def first_non_consecutive(arr):

    for i in range(len(arr)):
        if (i == 0):
            continue
        else:
            if (arr[i] - arr[i-1] != 1):
                return arr[i]    
    return None
