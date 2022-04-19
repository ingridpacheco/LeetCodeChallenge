# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.nodes = {}
        self.values = []
    
    def traverse_tree(self, root: Optional[TreeNode]) -> None:
        if root.left is not None: 
            self.traverse_tree(root.left)
                
        self.values.append(root.val)
        self.nodes[len(self.values) - 1] = root
        
        if root.right is not None:
            self.traverse_tree(root.right)
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.traverse_tree(root)
        
        first_index = 0
        second_index = len(self.values) - 1
        
        while first_index < len(self.values) - 1 and self.values[first_index] < self.values[first_index + 1]:
            first_index += 1
        
        while second_index > 0 and self.values[second_index] > self.values[second_index - 1]:
            second_index -= 1
            
        self.nodes[first_index].val, self.nodes[second_index].val = self.nodes[second_index].val, self.nodes[first_index].val