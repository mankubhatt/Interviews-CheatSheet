from collections import deque

def fn(graph):
    start_node, ans = 0, 0
    q = deque([start_node])
    visit = {start_node}

    while q:
        node = q.popleft()
        for nei in graph[node]:
            if nei not in visit:
                visit.add(nei)
                q.appen(nei)
    return ans 