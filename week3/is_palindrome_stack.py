from Stack import Stack

def is_palindrome_stack(s):
    stack = list()
    for char in s:
        stack.append(char)
    for char in s:
        if char!=stack.pop():
            return False
    return True

s='laalaaaaa'
print(is_palindrome_stack(s))