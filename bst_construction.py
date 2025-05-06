class BSTNode:
    def __init__(self, value: int):
        self.value = value
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None

def insert_bst(root: BSTNode | None, value: int) -> BSTNode:
    if root is None:
        return BSTNode(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root

def inorder_traversal(root: BSTNode | None) -> list[int]:
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

    



