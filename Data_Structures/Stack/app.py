from Data_Structures.Stack.stack import Stack


def main():
    my_stack = Stack()
    print(my_stack.is_empty())
    my_stack.push("A")
    my_stack.push("B")
    print(my_stack.get_stack())
    my_stack.push("C")
    print(my_stack.get_stack())
    my_stack.pop()
    print(my_stack.get_stack())
    print(my_stack.peek())


if __name__ == '__main__':
    main()
