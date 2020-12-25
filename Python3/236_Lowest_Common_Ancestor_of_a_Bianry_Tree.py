class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans

# # my solution is not as good as the above one
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#             self.ret = root

#             def findNode(cur = root):
#                 if not cur:
#                     return False

#                 if cur == p or cur == q:
#                     if findNode(cur.left) or findNode(cur.right):
#                         self.ret = cur
#                     return True

#                 left_ret = findNode(cur.left)
#                 right_ret = findNode(cur.right)
#                 if left_ret and right_ret:
#                     self.ret = cur
#                     return False
#                 return left_ret or right_ret

#             findNode()
#             return self.ret 