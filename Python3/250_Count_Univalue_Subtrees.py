# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.ret = 0
        
        def isUnivalTree(root):
            if not root:
                return True, None
            
            left, left_val = isUnivalTree(root.left)
            right, right_val = isUnivalTree(root.right)
            
            if left and right:
                if (not left_val and not right_val) or (not left_val and right_val == root.val) or (not right_val and left_val == root.val) or (root.val == left_val and left_val == right_val):
                    self.ret += 1
                    return True, root.val 
            
            return False, root.val
                
                
        isUnivalTree(root)
        
        return self.ret