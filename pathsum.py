# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def find(root,targetSum,count,res):
            if(root):
                print(count,root.val)
                count+=root.val
                if(not root.left and not root.right):
                    if(count==targetSum):
                        res=True
                        return res
                if(not res):
                    if(root.left):
                        res=find(root.left,targetSum,count,res)
                    if(root.right):
                        res=find(root.right,targetSum,count,res)
            else:
                return False
            return res
        res=False
        count=0
        res=find(root,targetSum,count,res)
        return res

        
                

        