from collections import deque


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # 깊이
        depth = 0
        maxDepth = 0

        # 노드 넣기
        Q = deque([root])

        while Q:
            for _ in range(len(Q)):
                cur_node = Q.popleft()
                if (cur_node.left.val == cur_node.val) or (cur_node.right.val == cur_node.val):
                    if cur_node.left.val == cur_node.val:
                        depth += 1

                    if cur_node.right.val == cur_node.val:
                        depth += 1

                    if depth > maxDepth:
                        maxDepth = depth

                else:
                    # 연결이 끝김
                    depth = 0
                    if cur_node.left:
                        Q.append(cur_node.left)
                    if cur_node.right:
                        Q.append(cur_node.right)

        return maxDepth
