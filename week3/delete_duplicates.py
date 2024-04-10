def delete_duplicates(s):
    stack = []
    for char in s:
        if not stack or char != stack[-1]:
            stack.append(char)
        elif char == stack[-1]:
            stack.pop()
    return ''.join(stack)

# Пример использования
input_str = "cdffd"
output_str = delete_duplicates(input_str)
print(output_str)

input_str = "uioouiouuo"
output_str = delete_duplicates(input_str)
print(output_str)

input_str = "xyyx"
output_str = delete_duplicates(input_str)
print(output_str)