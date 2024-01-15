def dfs(graph):
    start_node, ans = 0, 0
    stack = [start_node]
    seen = {start_node}

    while stack:
        node = stack.pop()
        for neig in graph[node]:
            if neig not in seen:
                seen.add(neig)
                stack.append(neig)

    return ans