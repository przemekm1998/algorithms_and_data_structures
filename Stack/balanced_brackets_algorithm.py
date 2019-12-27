from Stack.stack import Stack


def is_match(opening_bracket, closing_bracket):
    """
    Brackets checking for match
    """
    if opening_bracket == '(' and closing_bracket == ')':
        return True
    if opening_bracket == '{' and closing_bracket == '}':
        return True
    if opening_bracket == '[' and closing_bracket == ']':
        return True
    else:
        return False


def solution(brackets):
    """
    Checking the brackets string
    """
    opening_brackets = ('(', '{', '[')
    brackets_stack = Stack()

    is_balanced = True
    index = 0

    while index < len(brackets) and is_balanced:
        if brackets[index] in opening_brackets:
            brackets_stack.push(brackets[index])
        else:
            if not brackets_stack.is_empty():
                top_element = brackets_stack.pop()
                if not is_match(top_element, brackets[index]):
                    is_balanced = False
            else:
                is_balanced = False
        index += 1

    return is_balanced


def main():
    brackets = '((()))'
    print(solution(brackets))
    siema = 'eluwa'
    print(siema[::-1])


if __name__ == '__main__':
    main()
