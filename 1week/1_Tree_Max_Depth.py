from collections import deque


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        # 깊이
        depth = 0

        # 노드 넣기
        Q = deque([root])

        while Q:
            depth += 1

            print("----------")
            print(len(Q))
            for _ in range(len(Q)):
                cur_node = Q.popleft()
                print(cur_node)
                if cur_node.left:
                    Q.append(cur_node.left)
                    print("cur_node.left ", cur_node.left)
                if cur_node.right:
                    Q.append(cur_node.right)
                    print("cur_node.right ", cur_node.right)

        return depth