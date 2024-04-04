class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first=None, second=None):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head:
        raise ValueError
    if not head.next:
        raise ValueError

    cursor = head
    a_prev = None
    b_prev = None
    flag = True
    while cursor:
        if flag:
            node_a = Node(cursor.data)
            if a_prev:
                a_prev.next = node_a
            else:
                a_new = node_a
            a_prev = node_a
            flag = False
        else:
            node_b = Node(cursor.data)
            if b_prev:
                b_prev.next = node_b
            else:
                b_new = node_b
            b_prev = node_b
            flag = True
        cursor = cursor.next

    return Context(a_new, b_new)