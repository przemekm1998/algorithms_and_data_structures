from Data_Structures.Stack.stack import Stack


def solution(number):
    """
    Params: Positive integer number
    Return: Binary conversion of input number
    Converting input decimal to binary output
    """

    if number > 0:
        binary_stack = Stack()

        while number != 0:
            digit = number % 2
            binary_stack.push(digit)
            number = int(number / 2)

        result = ''

        while not binary_stack.is_empty():
            result += str(binary_stack.pop())

        return result
    else:
        return 0


def main():
    print(solution(242))
    print(int(solution(242), 2) == 242)


if __name__ == '__main__':
    main()
