"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if root == None:
            return root
        
        nodes = [root]
        nodes_levels = [[root]]
        index = 0
        
        while len(nodes) != 0:
            cur_node = nodes.pop(0)
            node_index = nodes_levels[index].index(cur_node)
            if node_index == 0:
                nodes_levels.append([])
            
            if cur_node.left != None:
                nodes_levels[index + 1].append(cur_node.left)
                nodes.append(cur_node.left)
                
            if cur_node.right != None:
                nodes_levels[index + 1].append(cur_node.right)
                nodes.append(cur_node.right)

            if node_index != len(nodes_levels[index]) - 1:
                cur_node.next = nodes_levels[index][node_index + 1]
            else:
                cur_node.next = None
                index += 1
                
        return root

    def improved_connect(self, root):

        """
        :type root: Node
        :rtype: Node
        """
        
        if root == None:
            return root
        
        index = 0
        none_index = 0
        nodes = [root]
        
        while len(nodes) != 0:
            node = nodes.pop(0)
            if node.left != None:
                nodes.append(node.left)
            if node.right != None:
                nodes.append(node.right)
            
            if index == none_index:
                node.next = None
                none_index = (none_index + 1) * 2
            else:
                node.next = nodes[0]
                
            index += 1  

        return root