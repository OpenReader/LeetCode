# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        
        def bst(root):
            st = []
            cur = root
            while cur:
                st.append(cur)
                cur = cur.left
            while st:
                cur = st.pop()
                yield cur.val
                cur = cur.right
                while cur:
                    st.append(cur)
                    cur = cur.left
                                   
        ret = deque()
        tree = bst
        for n in tree(root):
            if len(ret) < k:
                ret.append(n)
            else:
                if abs(n - target) < abs(ret[0] - target):
                    ret.popleft()
                    ret.append(n)
                else:
                    break
        
        return ret