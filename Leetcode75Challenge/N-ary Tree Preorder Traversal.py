def preorder(root):
    if root is None:
        return []
    values = []
    values.append(root.val)
    for child in root.children:
        values.extend(preorder(child))
    return values

