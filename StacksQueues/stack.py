class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    # print the stack
    def print_stack(self):
        print(self.stack)


def reverse_string(text):
    stack = Stack()
    for ch in text:
        stack.push(ch)
    result = ""
    while rev_ch := stack.pop():
        result += rev_ch
    return result


def infix_to_postfix(infix):

    operators = {'-': 1, '+': 2, '*': 3, '%': 4}

    stack = Stack()
    postfix = ''

    for ch in infix:
        if ch not in operators:
            postfix += ch
            continue
        if stack.is_empty():
            stack.push(ch)
            continue

        while not stack.is_empty() and operators[ch] <= operators[stack.peek()]:
            postfix += stack.pop()
        stack.push(ch)

    while not stack.is_empty():
        postfix += stack.pop()

    return postfix


# input_string = input("Enter a string to reverse: ")
# reversed_string = reverse_string(input_string)
# print(f"Original string: {input_string}")
# print(f"Reversed string: {reversed_string}")

expression = input()
print(f'{infix_to_postfix(expression)}')
