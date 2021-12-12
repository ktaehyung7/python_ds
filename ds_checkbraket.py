def check_braket(text):
    stack=[]
    for idx, letter in enumerate(text):
        if letter == '(':
            stack.append(idx)
        elif letter == ')':
            if stack:
                stack.pop()
            else:
                stack.append(idx)
                return stack
    return stack
