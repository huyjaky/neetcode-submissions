# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Perform an in-order traversal of the BST
        stack = []
        current = root
        
        while True:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Pop the node from the stack
            current = stack.pop()
            k -= 1
            
            # If we've reached the kth smallest element
            if k == 0:
                return current.val
            
            # Move to the right subtree
            current = current.right
        