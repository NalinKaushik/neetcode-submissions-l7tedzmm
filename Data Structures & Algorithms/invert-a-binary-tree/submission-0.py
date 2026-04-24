from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        temp = root
        q.append(temp)
        while(len(q)!=0):
            node = q.popleft()
            if node:
                node.left, node.right = node.right, node.left
                q.extend([node.right,node.left])
        return root

        
