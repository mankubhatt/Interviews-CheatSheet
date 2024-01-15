# Two pointers: one input, opposite ends

def fn(arr):
    l, r = 0, len(arr) - 1
    ans = 0
    while l < r:
        # do some logic here with left and right
        if 'CONDITION':
            l += 1
        else:
            r -= 1

    return ans



# Two pointers: two inputs, exhaust both

def fn(arr1, arr2):
    i, j = 0, 0
    ans = 0

    while i < len(arr1) and j < len(arr2):
        # do some logic here
        if 'CONDITION':
            i += 1
        else:
            j += 1
    
    if i < len(arr1):
        # do some logic here
        i += 1

    if j < len(arr2):
        # do some logic here
        j += 1

    return ans
