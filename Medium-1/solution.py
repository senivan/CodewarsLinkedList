""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    flag = False
    current = head
    last = current
    if head is None:
        return Node(data)
    if data < head.data:
        tmp = Node(data)
        tmp.next = head
        return tmp
    while current is not None and current.next is not None:
        if data > current.data and data < current.next.data:
            tmp = Node(data)
            tmp.next = current.next
            current.next = tmp
            flag = True
            break
        last = current.next
        current = current.next
    if not flag:
        last.next = Node(data)
    return head