import unittest
from Data_Structures.Doubly_LL.doubly_ll import DoublyLinkedList


class DoublyLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.dlist = DoublyLinkedList()

    def test_if_empty(self):
        """ Empty dlist case """

        self.assertEqual(str(self.dlist), str([]))

    def test_append(self):
        """ Appending test """

        self.dlist.append(2)
        self.dlist.append(3)
        self.assertEqual(str(self.dlist), str([2, 3]))

    def test_prepend(self):
        """ Prepending test """

        self.dlist.append(2)
        self.dlist.append(3)
        self.dlist.prepend(4)
        self.assertEqual(str(self.dlist), str([4, 2, 3]))

    def test_add_node_after_having_next(self):
        """ Add node after value that has next element """

        self.dlist.append(2)
        self.dlist.append(3)
        self.dlist.add_node_after(key=2, data=4)
        self.assertEqual(str(self.dlist), str([2, 4, 3]))

    def test_add_node_after_not_having_next(self):
        """ Add node after value that has no next element """

        self.dlist.append(2)
        self.dlist.append(3)
        self.dlist.add_node_after(key=3, data=4)
        self.assertEqual(str(self.dlist), str([2, 3, 4]))

    def test_add_before_node_head(self):
        """ Add before head """

        self.dlist.append(2)
        self.dlist.append(3)

        self.dlist.add_before_node(key=2, data=4)
        self.assertEqual(str(self.dlist), str([4, 2, 3]))

    def test_add_before_node_not_head(self):
        """ Add before any """

        self.dlist.append(2)
        self.dlist.append(3)

        self.dlist.add_before_node(key=3, data=5)
        self.assertEqual(str(self.dlist), str([2, 5, 3]))

    def test_delete_node_only_one_present(self):
        """ Case 1: Deleting the only one present node """

        self.dlist.append(2)
        self.dlist.delete_node(2)
        self.assertEqual(str(self.dlist), str([]))

    def test_delete_node_head(self):
        """ Case 2: Deleting the head node """

        self.dlist.append(2)
        self.dlist.append(3)
        self.dlist.delete_node(2)
        self.assertEqual(str(self.dlist), str([3]))

    def test_delete_node_not_head_having_next(self):
        """ Case 3: Deleting node other than head having next"""

        self.dlist.append(3)
        self.dlist.append(2)
        self.dlist.append(4)
        self.dlist.delete_node(2)
        self.assertEqual(str(self.dlist), str([3, 4]))

    def test_delete_node(self):
        """ Case 4: Deleting node other than head not having next"""

        self.dlist.append(3)
        self.dlist.append(2)
        self.dlist.append(4)
        self.dlist.delete_node(4)
        self.assertEqual(str(self.dlist), str([3, 2]))

    def test_reverse(self):
        self.dlist.append(2)
        self.dlist.append(3)
        self.dlist.append(4)
        self.dlist.reverse()
        self.assertEqual(str(self.dlist), str([4, 3, 2]))

    def test_remove_duplicates(self):
        self.dlist.append(8)
        self.dlist.append(4)
        self.dlist.append(4)
        self.dlist.append(6)
        self.dlist.append(4)
        self.dlist.append(8)
        self.dlist.append(4)
        self.dlist.append(10)
        self.dlist.append(12)
        self.dlist.append(12)
        self.dlist.remove_duplicates()
        self.assertEqual(str(self.dlist), str([6, 8, 4, 10, 12]))

    def test_pairs_with_sum(self):
        self.dlist.append(1)
        self.dlist.append(2)
        self.dlist.append(3)
        self.dlist.append(4)
        self.dlist.append(5)
        self.dlist.append(0)
        returned = self.dlist.pairs_with_sum(5)
        true = {2: 3,
                1: 4,
                5: 0}
        self.assertEqual(returned, true)


if __name__ == '__main__':
    unittest.main()
