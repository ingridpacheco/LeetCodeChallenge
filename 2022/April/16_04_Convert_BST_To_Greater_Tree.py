# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.sum_values = 0
    
    def get_node_value(self,root):
        
        if root.right is not None:
            root.right = self.get_node_value(root.right)
        self.sum_values += root.val
        root.val = self.sum_values
        if root.left is not None:
            root.left = self.get_node_value(root.left)
            
        return root
        
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return root
        
        return self.get_node_value(root)