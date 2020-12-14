# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, root: TreeNode) -> int:
        d = 0
        while root:
            root = root.left
            d += 1
        return d-1
    
    def exist(self, idx: int, d: int, root: TreeNode) -> bool:
        left, right = 0, 2 ** d - 1
        node = root
        for _ in range(d):
            mid = left + (right - left) // 2
            if idx <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
        return True if node else False
    
    def countNodes(self, root: TreeNode) -> int:   
        if not root:
            return 0
        d = self.getDepth(root)
        
        left, right = 0, 2**d - 1
        while left+1 < right:
            mid = left + (right - left) // 2
            if self.exist(mid, d, root):
                left = mid
            else:
                right = mid
        if self.exist(right, d, root):
            return 2 ** d + right
        return 2 ** d + left