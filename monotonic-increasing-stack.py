def fn(arr):
    stack = []
    ans = 0

    for n in arr:
        while stack and stack[-1] > n:
            stack.pop()
        stack.append(n)
    return ans
