class Tree:
    def __int__(self,val = None,left = None,right = None):
        self.val = val
        self.left =left
        self.right = right

    def isValidBST(self, root) -> bool:
        def dfs(node,left,right):
            if not node:
                return True
            if not (left < node.val and node.val < right):
                return False
            if not dfs(node.left, left, node.val):
                return False
            if not dfs(node.right,left,node.right):
                return False

        return dfs(root,float('-inf'),float('inf'))

