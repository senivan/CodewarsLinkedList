from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if node is None:
        raise ValueError()
    if index < 0:
        raise ValueError()
    for i in range(index):
        node = node.next
        if node is None:
            raise ValueError()
    return node