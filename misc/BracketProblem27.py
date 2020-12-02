def validator(user_input):
    stack = []
    is_valid = True
    for char in user_input:
        if char == '[' or char == '(' or char == '{':
            stack.append(char)
        elif char == ']' or char == '}' or char == ')':
            if len(stack) == 0:
                is_valid = False
                break
            if char != get_bracket_mirror(stack.pop()):
                is_valid = False
                break
        else:
            print("Invalid Chars..")
            break
    if len(stack) == 0:
        if is_valid:
            return True
        else:
            return False
    else:
        return False


def get_bracket_mirror(char):
    if char == '[':
        return ']'
    elif char == '{':
        return '}'
    elif char == '(':
        return ')'
    else:
        return '!'


if __name__ == '__main__':
    val = input("Enter the String : ")
    print(validator(val))
