def fn(graph):
    visit = set()
    def dfs(node):
        visit.add(node)
        # do some logic
        for neig in graph[node]:
            if neig not in visit:
                ans += dfs(neig)

        return ans
    return dfs(0)