# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        count=0
        mini=10000
        def min(root,mini,count):
            if(root):
                count+=1
                if(root.left):
                    mini=min(root.left,mini,count)
                if(root.right):
                    mini=min(root.right,mini,count)
                if(not root.left and not root.right):
                    if(mini>count):
                        mini=count
                        return mini
            else:
                mini=0
            return mini
        mini=min(root,mini,count)
        return mini
            



        