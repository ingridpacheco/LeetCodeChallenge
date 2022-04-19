# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.cur_node = TreeNode()
        self.order_tree = self.cur_node
    
    def getOrderBST(self, root: TreeNode) -> None:
        
        if root.left is not None:
            self.getOrderBST(root.left)
            
        self.cur_node.right = TreeNode(root.val)
        self.cur_node = self.cur_node.right
            
        if root.right is not None:
            self.getOrderBST(root.right)
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        self.getOrderBST(root)
        return self.order_tree.right