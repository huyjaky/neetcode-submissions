# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: if the root is None, return None
        if not root:
            return None
        
        # If either p or q is the root, then root is the LCA
        if root == p or root == q:
            return root
        
        # Recur for left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right LCA are not None, then root is the LCA
        if left_lca and right_lca:
            return root
        
        # Otherwise return the non-null child
        return left_lca if left_lca else right_lca
        