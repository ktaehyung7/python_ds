def factorial(n):
    if n==1 :
        return n
    return n*factorial(n-1)

def fact(n):
    stack=[]
    while n > 0:
        stack.append(n)
        n -=1
    result =1
    while stack:
        result *= stack.pop()
    return result

def fact1(n):
    result=1
    for i in range(1, n+1):
        result *= i
    return result

def recur(n):
    print(n)
    return recur(n+1)
