from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    if head is None:
        return Node(data)
    if not isinstance(head, Node):
        temp = Node(head)
        temp.next = data
        return temp
    result = Node(data)
    result.next = head
    return result
def build_one_two_three():
    # Your code goes here.
    return push(push(push(None, 3),2),1)