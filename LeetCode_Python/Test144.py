__author__ = 'zyt'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        list = []
        if root:
            list += root.val,
            list += self.preorderTraversal(root.left)
            list += self.preorderTraversal(root.right)
        return list
