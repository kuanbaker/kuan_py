#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#leetcode 515. Find Largest Value in Each Tree Row

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        que_bfs = [root]
        result = []
        if root:
            while len(que_bfs) > 0:
                max_val = -inf
                size = len(que_bfs)
                for i in range(size):
                    ele = que_bfs.pop(0)
                    max_val = max(ele.val, max_val)
                    if ele.left:
                        que_bfs.append(ele.left)
                    if ele.right:
                        que_bfs.append(ele.right)
                result.append(max_val)
        return result

    
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n3
n1.right = n2
n3.left = TreeNode(5)
n3.right = TreeNode(3)
n2.right = TreeNode(9)

