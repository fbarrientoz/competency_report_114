class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.val)


class DoubleLinkedList:
    def __init__(self, val):
        self.head = Node(val)

    def __str__(self):
        result = ""
        tmp = self.head
        while tmp:
            result += str(tmp.val) + (' --> ' if tmp.next else '')
            tmp = tmp.next
        return result

    def find(self, value, base_node=None, foward=True):
        if not base_node:
            base_node = self.head

        while base_node:
            if base_node.val == value:
                return base_node

            if foward:
                base_node = base_node.next
            else:
                base_node = base_node.prev

    def append(self, val):
        tmp = self.head
        if not tmp:
            return

        while tmp.next:
            tmp = tmp.next

        tmp.next = Node(val)
        tmp.next.prev = tmp
        
        return tmp.next

    def prepend(self, val):
        if not self.head:
            return

        self.head.prev = Node(val)
        self.head.prev.next = self.head
        self.head = self.head.prev

    def remove(self, value, node=None):
        nd = node if node else self.find(value)
        if nd:
            if nd.prev:
                nd.prev.next = nd.next
            if nd.next:
                nd.next.prev = nd.prev
                if nd == self.head:
                    self.head = nd.next
        else:
            raise Exception("Invalid base node.")

    def insert(self, find_value, value, after_insted_of_before=True, node=None):
        nd = node if node else self.find(find_value)
        res_node = Node(value)
        if nd:
            if after_insted_of_before:
                n0 = nd
                n1 = nd.next
            else:
                n0 = nd.prev
                n1 = nd

            if n0:
                n0.next = res_node
            if n1:
                n1.prev = res_node

            res_node.prev = n0
            res_node.next = n1
        else:
            raise Exception("Error")


if __name__ == '__main__':
    ts = DoubleLinkedList(6)
    ts.append(15)
    ts.append(26)
    ts.append(17)

    ts.prepend(38)
    ts.prepend(-1)

    ts.remove(15)
    ts.remove(17)

    ts.insert(26, -25)
    ts.insert(26, -24, False)

    assert ts.find(-1, ts.find(17), False).val == -1, "Sfind"
    print(ts)
