def postfix(expression):
    stack=[]
    for element in expression:
        if element == "+":
            op2, op1=pop_pop(stack)
            stack.append(op1+op2)
        elif element == "-":
            op2, op1=pop_pop(stack)
            stack.append(op1-op2)
        elif element == "*":
            op2, op1=pop_pop(stack)
            stack.append(op1*op2)
        elif element == "/":
            op2, op1=pop_pop(stack)
            stack.append(op1/op2)
        else:
            stack.append(int(element))
    return stack.pop()

def pop_pop(stack):
    op2=stack.pop()
    op1=stack.pop()
    return op2, op1