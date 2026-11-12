# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res=[]

        def recursion(d,node):
            if not node: 
                return []
            if len(res)==d:
                res.append([])

            res[d].append(node.val)
            dfs(node.left,d+1)
            dfs(node.right,d+1)
        
        df(0,root)
        return res
        
            
