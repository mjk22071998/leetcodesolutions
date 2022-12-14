# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        depth = 0
        while q:
            level_size = len(q)
            depth += 1
            for _ in range(level_size):
                curr = q.popleft()
                if not curr.left and not curr.right:
                    return depth
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
        return depth