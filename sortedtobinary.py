# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        size=len(nums)//2
        idx=0
        node=TreeNode(nums[size],None,None)
        
        def built(num,node):
            if(num<node.val):
                if(node.left):
                    built(num,node.left)
                else:
                    node.left=TreeNode(num,None,None)
            if(num>node.val):
                if(node.right):
                    built(num,node.right)
                else:
                    node.right=TreeNode(num,None,None)
        def sort(nums,node):
            if(len(nums)>1):
                size=len(nums)//2
                built(nums[size],node)
                
                sort(nums[0:size],node)
                sort(nums[size:len(nums)],node)
            else:
                built(nums[0],node)
        sort(nums,node)

        return node
        
            
        


        
        