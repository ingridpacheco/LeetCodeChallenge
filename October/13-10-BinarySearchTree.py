# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    
    def insert(self, root, value):
        if (root == None):
            return TreeNode(value)
        if (value > root.val):
            root.right = self.insert(root.right, value)
        else:
            root.left = self.insert(root.left, value)
        return root
    
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        
        root = None
        
        for number in preorder:
            root = self.insert(root, number)
        
        # ordered_list = [root]
        
        # while(lk):
#         for i,v in enumerate(ordered_list):
#             if v != None:
#                 ordered_list[i] = v.val
#                 if (v.left != None or v.right != None):
#                     ordered_list.append(v.left)
#                     ordered_list.append(v.right)
            
        return root