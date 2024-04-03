def stringify(node):
    result = ""
    if node is None:
        return "None"
    while node.data is not None:
        result += f"{node.data} -> "
        if node.next is None:
            break
        node = node.next
    result += "None"
    return result