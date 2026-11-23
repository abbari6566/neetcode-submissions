from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #base case
        if not root:
            return []

        result = []
        #start with root
        queue = deque([root])

        while queue:
            #append the rightmost first since queue, queue[0] will always give right
            result.append(queue[0].val)
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)

        return result

#Time & space - O(n, where n = # of nodes) & O(w, where w is the max width of the tree)
        