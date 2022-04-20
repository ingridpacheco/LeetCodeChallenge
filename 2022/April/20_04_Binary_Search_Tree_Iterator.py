# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.values = []
        self.getInOrderValues(root)
        
    def getInOrderValues(self, root: Optional[TreeNode]) -> TreeNode:
        if root.left is not None:
            self.getInOrderValues(root.left)
        
        self.values.append(root.val)
        
        if root.right is not None:
            self.getInOrderValues(root.right)

    def next(self) -> int:
        val = self.values.pop(0)
        return val

    def hasNext(self) -> bool:
        return len(self.values) != 0
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()