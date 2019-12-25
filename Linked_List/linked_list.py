class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next

    def insert_after_node(self, data, prev_node):
        if not prev_node:
            print('Previous node is not in the linked list')
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node
        # node_to_check = self.head
        #
        # inserted = False
        # while not inserted:
        #     if node_to_check.data == after_node:
        #         new_node.next = node_to_check.next
        #         node_to_check.next = new_node
        #         inserted = True
        #     else:
        #         node_to_check = node_to_check.next

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:  # Run until node is not None or not found
            prev = cur_node  # Keeping track of the prev node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head

            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

            previous = None
            count = 0

            while cur_node and count != pos:
                previous = cur_node
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return

            previous.next = cur_node.next
            cur_node = None

    def len_iterative(self):
        count = 0
        if self.head:
            cur_node = self.head
            while cur_node:
                cur_node = cur_node.next
                count += 1
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_values(self, value1, value2):
        if self.head and self.head.next is not None:
            if value1 == value2:
                return

            remember_value = None
            cur_node = self.head

            while cur_node:
                if cur_node.data == value1 or cur_node.data == value2:
                    if remember_value is None:
                        remember_value = cur_node
                    else:
                        remember_value_2 = cur_node.data
                        cur_node.data = remember_value.data
                        remember_value.data = remember_value_2
                        return
                cur_node = cur_node.next

            if cur_node is None:
                return

    def inverse_recursive(self):

        def _inverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _inverse_recursive(cur, prev)

        self.head = _inverse_recursive(cur=self.head, prev=None)

    def inverse_iteration(self):
        if self.head:
            cur = self.head
            prev = None
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            self.head = prev

    @staticmethod
    def merge_lists(list1, list2):
        merged_list = LinkedList()
        p = list1.head
        q = list2.head
        while p or q:
            if p is None:
                merged_list.append(q.data)
                q = q.next
            if q is None:
                merged_list.append(p.data)
                p = p.next
            else:
                if q.data <= p.data:
                    merged_list.append(q.data)
                    q = q.next
                else:
                    merged_list.append(p.data)
                    p = p.next
        return merged_list

    def remove_duplicates(self):
        """
        Removing duplicates from the list
        """
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                # Remove node:
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before.
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def print_nth_from_last(self, n):
        """
        Getting the nth node from the last node
        """
        if self.head:
            cur = self.head
            llist_length = self.len_iterative()
            length = llist_length - n
            if length < 0:
                err = 'Error: {} is beyond the length of the array - {}'.format(n, llist_length)
                print(err)
                return

            for i in range(0, length):
                cur = cur.next

            print(cur.data)

    def count_occurance(self, data):
        """
        Counting a number of occurance of a given data
        """
        count = 0
        if self.head:
            cur = self.head
            while cur:
                if cur.data == data:
                    count += 1
                cur = cur.next
        return count

    def count_occurance_recursive(self, node, data):
        if not node:
            return 0
        elif node.data == data:
            return 1 + self.count_occurance_recursive(node.next, data)
        elif node.data != data:
            return self.count_occurance_recursive(node.next, data)

    def rotate(self, data):
        """
        Rotate the linked list around an inserted pivot point
        """
        if self.head:
            new_tail = None
            link_cur_head = None
            cur = self.head

            while cur is not None:
                if cur.data == data:
                    new_tail = cur
                if cur.next is None:
                    link_cur_head = cur
                cur = cur.next

            if new_tail is None:
                return
            else:
                link_cur_head.next = self.head
                self.head = new_tail.next
                new_tail.next = None

    def is_palindrome_string(self):
        s = ""
        p = self.head

        while p:
            s += p.data
            p = p.next

        return s == s[::-1]

    def is_palindrome_stack(self):
        if self.head:
            s = []
            p = self.head
            while p:
                s.append(p.data)
                p = p.next
            p = self.head
            while p:
                data = s.pop()
                if data != p.data:
                    return False
                p = p.next
            return True

    def move_tail_to_head(self):
        """
        Moving the last element to become the head of linked list
        """
        if self.head and self.head.next:
            cur = self.head
            prev = None

            while cur.next:
                prev = cur
                cur = cur.next

            prev_head = self.head
            self.head = cur
            self.head.next = prev_head
            prev.next = None

    @staticmethod
    def sum_two_lists(digit1, digit2):
        p = digit1.head
        q = digit2.head

        result = LinkedList()
        temp_res = 0
        change = 0

        while p or q:
            if p is None:
                temp_res = q.data + change
            elif q is None:
                temp_res = p.data + change
            else:
                temp_res = q.data + p.data + change

            if temp_res >= 10:
                change = int(temp_res / 10)
                temp_res = temp_res - (10 * change)
            else:
                change = 0

            result.append(temp_res)

            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        if change != 0:
            result.append(change)

        return result


def fibonacci(self, number):
    if number <= 1:
        return number
    else:
        return self.fibonacci(number - 1) + self.fibonacci(number - 2)


def is_string_palindrome(str1):
    string2 = str1[::-1]
    return string2 == str1


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("X")

# print(str(llist.len_iterative()))
# print(str(llist.len_recursive(llist.head)))

# llist.insert_after_node('Z', 'C')
# llist.insert_after_node('D', llist.head.next)
#
# print("Before delete")
# llist.print_list()
#
# print("After delete")
# llist.delete_node('A')
# llist.print_list()
#
# print("After delete at pos")
# llist.delete_node_at_pos(4)
# llist.print_list()

# for i in range(0, 10):
#     print(str(llist.fibonacci(i)))

# llist.swap_values('B', 'B')
# llist.print_list()

# llist.inverse_recursive()
# llist.print_list()

# llist_1 = LinkedList()
# llist_2 = LinkedList()
#
# llist_1.append(1)
# llist_1.append(5)
# llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)
#
# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)
#
# merged_lists = LinkedList.merge_lists(llist_1, llist_2)
# merged_lists.print_list()

# llist_3 = LinkedList()
# llist_3.append(3)
# llist_3.append(3)
# llist_3.append(2)
# llist_3.remove_duplicates()
# llist_3.print_list()

llist_2 = LinkedList()
llist_2.append(5)
llist_2.append(6)
llist_2.append(3)
# llist_2.print_list()


llist_3 = LinkedList()
llist_3.append(8)
llist_3.append(4)
llist_3.append(2)
llist_3.append(5)
# llist_2.print_nth_from_last(20)
# print(str(llist_2.count_occurance(9)))
# print(str(llist_2.count_occurance_recursive(llist_2.head, 8)))

# llist_2.rotate(5)
# llist_2.print_list()

# print(str(llist_2.is_palindrome_stack()))
#
# llist_2.move_tail_to_head()
# llist_2.print_list()

sumed = LinkedList.sum_two_lists(llist_2, llist_3)
sumed.print_list()
