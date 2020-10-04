class Node:
    def __init__(self):
        self.next = None
        self.previous = None
        self.value = None

    # for creating a linked list you have to make a constant head and never change the head value


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = None

    def add(self, value):
        node = Node()
        node.value = value

        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node  # at the first time this will also create a next node for head node
            # and continuously this will make a linked list by jumping from one node to another and creating a next
            # node for each
            node.previous = self.head
            self.tail = node  # here every next node for previous tail.next node is also equal to this new tail after
            # jump
            # and creating next node for every tail will also connect with this tail node

    # def __str__(self):
    #     vals = []
    #     node = self.head
    #     while node.next is not None:
    #         vals.append(node.value)
    #         node = node.next
    #     print(vals)

    def print(self):
        vals = []
        node = self.head  # staring from head node.
        # We cannot run the loop depends on head. because the head must be constant at every point
        while node.next is not None:
            vals.append(node.value)
            node = node.next  # jumping from one node to another
        vals.append(node.value)  # we need to add last node as manually because loop is broken because
        # next node for this node is None/null
        print(vals)


linkedList = DoubleLinkedList()
linkedList.add(21)
linkedList.add(22)
linkedList.add(33)
linkedList.add(44)
linkedList.print()
