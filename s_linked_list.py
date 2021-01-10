
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self, val):
        self.head = Node(val)

    def __str__(self):
        result = ""
        tmp = self.head
        while tmp:
            result += str(tmp.val) + (' --> ' if tmp.next else '')
            tmp = tmp.next
        return result

    def append(self, val, after_node=None):
        tmp = self.head
        if not tmp:
            return

        while tmp.next and not(after_node is None and tmp.val == after_node):
            tmp = tmp.next
        another = tmp.next
        tmp.next = Node(val)
        tmp.next.next = another

    def prepend(self, val):
        nd = Node(val)
        nd.next = self.head
        self.head = nd

    def remove(self, value):
        nd = self.head
        if not nd:
            return

        if nd.val == value:
            self.head = nd.next

        while nd.next:
            if nd.next.val == value:
                nd.next = nd.next.next

            nd = nd.next


if __name__ == '__main__':
    ts = LinkedList(6)
    ts.append(10)
    ts.append(21)
    ts.append(12)
    ts.append(33, 10)

    ts.prepend(-1)

    ts.remove(10)

    print(ts)
