# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.ret = 0
        
        def longestTo(cur):
            left_len = right_len = 0
            if cur.left:
                left_len = longestTo(cur.left)
                if cur.left.val != cur.val + 1:
                    left_len = 0

            if cur.right:
                right_len = longestTo(cur.right)
                if cur.right.val != cur.val + 1:
                    right_len = 0

            longest_cur = max(left_len, right_len) + 1
            self.ret = max(longest_cur, self.ret)
            
            return longest_cur
        
        if root: longestTo(root)
        
        return self.ret