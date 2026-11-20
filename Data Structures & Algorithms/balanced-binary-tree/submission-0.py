# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(cur_node):

            if not cur_node:
                return 0
            
            left_subtree = dfs(cur_node.left)

            if self.balanced is False:
                return 0

            right_subtree = dfs(cur_node.right)

            if abs(left_subtree - right_subtree) > 1:
                self.balanced = False
                return 0

            return 1 + max(left_subtree, right_subtree)
        
        dfs(root)
        
        return self.balanced

# Time - O(n) and Space - O(height)