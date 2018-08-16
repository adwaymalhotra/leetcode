class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        
        while True:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            else:
                if not stack: return res
                else:
                    root = stack[-1]
                    stack = stack[:-1]
                    root = root.right

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                if not stack: return res
                else:
                    root = stack[-1]
                    stack = stack[:-1]
                    res.append(root.val)
                    root = root.right

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [(root, False)]
        result = []
        
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    result.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    
        return result
