def levelOrder(root):
    if not root:
        return []

    result = []
    current_result = []

    while current_result:
        next_level = []
        level_values = []

        for node in current_result:
            level_values.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        result.append(level_values)
        current_result = next_level

    return result
