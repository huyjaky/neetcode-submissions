# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # value -> vị trí của value trong inorder
        inorder_map = {
            value: i
            for i, value in enumerate(inorder)
        }

        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            # Không còn node
            if left > right:
                return None

            # Node đầu tiên trong preorder là root
            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)

            # Vị trí root trong inorder
            mid = inorder_map[root_value]

            # Xây LEFT trước
            root.left = build(left, mid - 1)

            # Sau đó xây RIGHT
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)