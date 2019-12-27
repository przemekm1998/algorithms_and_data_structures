from Linked_List.linked_list import LinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        """
        Append on the first place in the list
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            tail = self.head
            while tail.next is not self.head:
                tail = tail.next
            new_node.next = self.head
            self.head = new_node
            tail.next = self.head

    def append(self, data):
        """
        Append on the last place in the list
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next is not self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        """
        Print every element of the list
        """
        if self.head:
            cur = self.head

            while cur:
                print(str(cur.data))
                cur = cur.next
                if cur == self.head:
                    break

    def delete_node(self, data):
        """
        Deleting selected node with input data
        """
        if self.head:
            if data == self.head.data:
                cur = self.head

                if cur.next is self.head:
                    cur = None
                    return

                while cur:
                    cur = cur.next
                    if cur.next is self.head:
                        break

                self.head = self.head.next
                cur.next = self.head
            else:
                cur = self.head.next
                prev = self.head

                while cur:
                    if cur.data == data:
                        nxt = cur.next
                        prev.next = nxt
                        cur = None
                        return

                    cur = cur.next
                    prev = prev.next
                    if prev.next is self.head:
                        return

    def remove_node(self, node):
        if self.head:
            prev = self.head
            cur = self.head.next
            while cur:
                if cur == node:
                    if cur == self.head:
                        self.head = cur.next
                        prev.next = self.head
                        cur = None
                        return
                    else:
                        prev.next = cur.next
                        cur = None
                        return
                cur = cur.next
                prev = prev.next
                if cur == self.head.next:
                    return

    def josephus_circle(self, step):
        if step < 1:
            return

        cur = self.head

        while len(self) > 1:
            count = 1
            while count < step:
                cur = cur.next
                count += 1
            self.remove_node(cur)

    @staticmethod
    def is_circular(input_list):
        if input_list.head is None:
            return

        def __is_circular__(node):
            if node.next is None:
                return False
            elif node.next == input_list.head:
                return True
            else:
                return __is_circular__(node.next)

        return __is_circular__(input_list.head)

    @staticmethod
    def is_circular_iterative(input_list):
        if input_list.head is None:
            return

        cur = input_list.head
        while cur:
            if cur.next == input_list.head:
                return True
            cur = cur.next
        return False

    def __len__(self):
        if self.head:
            cur = self.head
            count = 1
            while cur:
                cur = cur.next
                if cur is self.head:
                    return count
                count += 1
            return count
        else:
            return 0


#  Appending, prepending, and printing
# cllist = CircularLinkedList()
# cllist.append("C")
# cllist.append("D")
# cllist.prepend("B")
# cllist.prepend("A")
# cllist.print_list()

#  Deleting the node
# cllist.delete_node("C")
# cllist.print_list()

#  Spliting into halves
# print(len(cllist))

#  Removing the node
# cllist.remove_node(cllist.head.next)

#  Josephus circle
# cllist2 = CircularLinkedList()
# cllist2.append(1)
# cllist2.append(2)
# cllist2.append(3)
# cllist2.append(4)
# cllist2.josephus_circle(2)
# cllist2.print_list()

# print(CircularLinkedList.is_circular(cllist2))
#
# llist = LinkedList()
# llist.append(2)
# llist.append(3)
# print(CircularLinkedList.is_circular_iterative(llist))
