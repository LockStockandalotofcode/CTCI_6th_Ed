# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Optimised Approach- pointers and hash map
        # create hash map 
        inorder_map = {val: index for index, val in enumerate(inorder)}
        
        # keep a global preorder_index to keep track of progress of tree made
        pre_idx = 0

        # define helper function depnding on pointers to inorder 
        def helper(in_start, in_end) -> Optional[TreeNode]:
            nonlocal pre_idx

            # Base case
            if in_start > in_end:
                return None

            # make treenode
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # increment preorder_index, after making a treenode
            pre_idx += 1

            # locate the index of this root in inorder array using hash map, to determine its left and right subtree
            mid = inorder_map[root_val]

            # recursively call helper function starting with entire inorder array
            root.left = helper(in_start, mid - 1)
            root.right = helper(mid + 1, in_end)

            return root
        
        return helper(0, len(inorder) - 1)