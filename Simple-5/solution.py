class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    # Your code goes here.
    # Remember to return the context.
    source_head = source.data
    dest_new = Node(source_head)
    dest_new.next = dest
    return Context(source.next, dest_new)