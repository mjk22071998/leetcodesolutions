# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self , tree,path=[])-> list:
        if tree.left!=None:
            self.DFS(tree.left,path)
        if tree.val!=None:
            path.append(tree.val)
        if tree.right!=None:
            self.DFS(tree.right,path)
        return path
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            return self.DFS(root,[])
        
        