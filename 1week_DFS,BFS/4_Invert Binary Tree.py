from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserialize(string):
    if string == "{}":
        return None
    nodes = [
        None if val == "null" else TreeNode(int(val))
        for val in string.strip("[]{}").split(",")
    ]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


test_cases = [
    {
        "input": deserialize("[4,2,7,1,3,6,9]"),
        "expect": deserialize("[4,7,2,9,6,3,1]"),
    },
    {
        "input": deserialize("[2,1,3]"),
        "expect": deserialize("[2,3,1]"),
    },
    {
        "input": [],
        "expect": [],
    },
]

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        Q = deque([root])

        while Q:
            cur_node = Q.popleft()
            if cur_node:
                cur_node.left, cur_node.right = cur_node.right, cur_node.left
                Q.append(cur_node.left)
                Q.append(cur_node.right)
        return root


solution = Solution()

for tc in test_cases:
    ok = tc["expect"] == solution.invertTree(root=tc["input"])
    if not ok:
        print(ok)
