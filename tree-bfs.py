from collections import deque

def bfs(root):
    q = deque([root])
    ans = 0

    while q:
        for _ in range(len(q)):
            # do some logic
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return ans