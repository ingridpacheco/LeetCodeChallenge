# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.counter = 0
        self.val = 0
    
    def walkTree(self, root: Optional[TreeNode], k: int) -> int:
        if root.left is not None:
            self.walkTree(root.left,k)
        
        self.counter += 1
        if self.counter == k:
            self.val = root.val
        
        if root.right is not None:
            self.walkTree(root.right,k)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.walkTree(root,k)
        return self.val