import unittest
from Stack.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.test_stack = Stack()

    def test_push(self):
        self.test_stack.push(5)
        self.assertEqual(self.test_stack.items, [5])

    def test_pop(self):
        self.test_stack.push(5)
        self.test_stack.pop()
        self.assertEqual(self.test_stack.items, [])

    def test_get_stack(self):
        self.test_stack.push(3)
        self.test_stack.push(2)
        self.assertEqual(self.test_stack.get_stack(), [3, 2])

    def test_is_empty(self):
        self.assertIs(self.test_stack.is_empty(), True)

        self.test_stack.push(5)
        self.assertIsNot(self.test_stack.is_empty(), True)

    def test_peek(self):
        self.test_stack.push(3)
        self.test_stack.push(2)
        self.test_stack.push(4)
        self.assertEqual(self.test_stack.peek(), 4)


if __name__ == '__main__':
    unittest.main()
