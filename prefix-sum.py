def fn(arr):
    prefix = [arr[0]]

    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + prefix[arr[i]])

    return prefix