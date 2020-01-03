from Data_Structures.Stack.stack import Stack


def solution(input_string):
    """
    Reversing the string using stack
    """
    stack = Stack()
    for i in range(0, len(input_string)):
        stack.push(input_string[i])

    rev_string = ""

    while not stack.is_empty():
        rev_string += stack.pop()

    return rev_string


def main():
    siema = 'eluwina'
    print(solution(siema))

if __name__ == '__main__':
    main()
