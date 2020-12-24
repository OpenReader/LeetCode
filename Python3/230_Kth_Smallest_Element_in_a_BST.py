# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.ret = 0
        self.k = k
        
        def helper(root):
            if not root or self.k == 0:
                return
            helper(root.left)
            self.k -= 1
            if self.k == 0:
                # print(root.val)
                self.ret = root.val
            helper(root.right)
        
        helper(root)   
        return self.ret