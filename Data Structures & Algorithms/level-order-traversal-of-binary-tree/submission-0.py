# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs -> Level order traversal
        if root is None:
            return None
        
from collections import deque
from typing import Optional, List

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: return an empty list if the tree is empty
        if root is None:
            return []
        
        traversal = [] 
        queue = deque([root])

        while queue:
            # 1. Get the number of nodes at the current level
            level_size = len(queue)
            current_level_vals = []
            
            # 2. Loop exactly 'level_size' times to process only this level
            for _ in range(level_size):
                curNode = queue.popleft()
                current_level_vals.append(curNode.val)

                # Add children for the NEXT level
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            
            # 3. Append the entire level as a single list
            traversal.append(current_level_vals)

        return traversal
        
'''
While loop combined with the for loop ensures that every single node in the tree is processed exactly once
- Time: O(N)
'''
        