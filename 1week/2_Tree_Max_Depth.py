from collections import deque


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # 깊이
        RightDepth = 0
        LeftDepth = 0

        # 노드 넣기
        Q = deque([root])
        RightQ = deque()
        LeftQ = deque()

        cur_node = Q.popleft()

        # 좌측 Depth
        if cur_node.left:
            RightQ.append(cur_node.left)
            while RightQ:
                RightDepth += 1
                for _ in range(len(RightQ)):
                    right_cur_node = RightQ.popleft()
                    if right_cur_node.left:
                        RightQ.append(right_cur_node.left)
                    if right_cur_node.right:
                        RightQ.append(right_cur_node.right)

        # 우측 Depth
        if cur_node.right:
            LeftQ.append(cur_node.right)
            while LeftQ:
                LeftDepth += 1
                for _ in range(len(LeftQ)):
                    left_cur_node = LeftQ.popleft()
                    if left_cur_node.left:
                        LeftQ.append(left_cur_node.left)
                    if left_cur_node.right:
                        LeftQ.append(left_cur_node.right)
        print(RightDepth, " : ", LeftDepth)
        return RightDepth + LeftDepth
