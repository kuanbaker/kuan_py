#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums == []:
            return None
    
        
        max_val = max(nums)
        max_index = nums.index(max_val)
        
        root = TreeNode(nums[max_index])
        left_tree = self.constructMaximumBinaryTree(nums[:max_index])
        right_tree = self.constructMaximumBinaryTree(nums[max_index+1:])
        
        root.left = left_tree
        root.right = right_tree
        
        return root

