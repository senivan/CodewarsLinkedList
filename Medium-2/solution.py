class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if head is None:
        return None
    if head.next is None:
        return Node(head.data)
    data = head.data
    head = reverse(head.next)
    current = None
    tmp = head
    while tmp is not None:
        current = tmp
        tmp = tmp.next
    current.next = Node(data)
    return head
        