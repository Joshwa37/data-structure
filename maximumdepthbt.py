# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        count=0
        max=0
        def depth(root,max,count):
            count+=1
            if(root):
                if(root.left):
                    max=depth(root.left,max,count)
                if(root.right):
                    max=depth(root.right,max,count)
                if not(root.left) and not(root.right):
                    if(max<count):
                        max=count
            print(max)
            return max
        max=depth(root,max,count)
        print(max)
        return max
        