def balanced_brackets(string: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in string:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack