import unittest
from Stack.stack import Stack


class TestStack(unittest.TestCase):

    def test_push(self):
        test_stack = Stack()
        test_stack.push(5)
        self.assertEqual(test_stack, [5])
