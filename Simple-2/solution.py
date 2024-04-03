def linked_list_from_string(s):
    if s is None or len(s) <= 1 or s == "None":
        return None
    list = s.split(' -> ')[:-1:]
    prev = Node(int(list[0]))
    if len(list) == 1:
        prev.next = None
        return prev
    result = None
    for index, element in enumerate(list[1:]):
        prev.next = Node(int(element))
        if index == 0:
            result = prev
        prev = prev.next
    return result