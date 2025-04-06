# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        def cou(root,count):
            if(root):
                count+=root.val
                if root.left:
                    count=cou(root.left,count)
                if root.right:
                    count=cou(root.right,count)
            return count
        count=0
        count=cou(root,count)
        def best(root,count):
            if root:
                if root.left:
                    count=best(root.left,count)
                prev=root.val
                root.val=count
                count-=prev
                if root.right:
                    count=best(root.right,count)
            return count
        count=best(root,count)
        return root
                
        

        