class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            return

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        if self.head:
            cur = self.head
            while cur:
                print(str(cur.data))
                cur = cur.next

    def add_node_after(self, key, data):
        """
        Adding node after a node with specified key
        """
        if self.head:
            new_node = Node(data)
            cur = self.head
            while cur.data != key:
                cur = cur.next
                if cur is None:
                    return
            new_node.next = cur.next
            new_node.prev = cur
            cur.next = new_node

    def add_before_node(self, key, data):
        """
        Adding node before a node with specified key
        """
        if self.head:
            new_node = Node(data)
            cur = self.head

            #  Adding node before head node
            if cur.data == key:
                self.head = new_node
                self.head.next = cur
                cur.prev = self.head

            #  Adding node before any node then head
            else:
                while cur.data != key:
                    cur = cur.next
                    if cur is None:
                        return
                cur.prev.next = new_node
                new_node.prev = cur.prev
                cur.prev = new_node
                new_node.next = cur

    def delete_node(self, key):
        if self.head:
            cur = self.head

            #  Case 1: Deleting the only one present node
            if cur.data == key and cur.next is None:
                self.head = None
                cur = None
                return

            #  Case 2: Deleting the head node
            if cur.data == key and cur.next:
                self.head = self.head.next
                self.head.prev = None
                cur = None
                return

            # Case 3 and 4
            else:
                while cur and cur.data != key:
                    cur = cur.next

                #  Key not found
                if not cur:
                    return

                    #  Case 3: Deleting node other than head having next
                if cur.next:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    cur = None
                    return

                    #  Case 4: Deleting node other than head not having next
                if not cur.next:
                    cur.prev.next = None
                    cur = None
                    return

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev

    def remove_duplicates(self):
        if self.head:
            values = dict()
            cur = self.head
            while cur:
                if cur.data not in values:
                    values[cur.data] = 1
                else:
                    self.delete_node(cur.data)
                cur = cur.next

    def pairs_with_sum(self, sum_to_pair):
        pairs = dict()

        if self.head:
            cur = self.head

            while cur:
                if cur.data <= sum_to_pair:
                    search = sum_to_pair - cur.data
                    if search in pairs and pairs[search] is None:
                        pairs[search] = cur.data
                    else:
                        pairs[cur.data] = None
                cur = cur.next

        return pairs

    def __str__(self):
        values = []
        if self.head:
            cur = self.head
            while cur:
                values.append(cur.data)
                cur = cur.next
        return str(values)
