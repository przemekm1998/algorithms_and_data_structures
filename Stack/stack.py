"""
The Stack Data Structure
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Append item at the end of the list
        """
        self.items.append(item)

    def pop(self):
        """
        Return the last element inserted to the list
        """
        return self.items.pop()

    def get_stack(self):
        """
        Returns the items
        """
        return self.items

    def is_empty(self):
        """
        Checks whether the stack is empty
        """
        return self.items == []

    def peek(self):
        """
        Return the top element of the stack
        """
        return self.items[-1]


