# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(not root):
            return True
        
        if(root.right!=None and root.right.val!=root.val):
            return False
        
        if(root.left!=None and root.left.val!=root.val):
            return False
        
        return self.isUnivalTree(root.right) and self.isUnivalTree(root.left)
