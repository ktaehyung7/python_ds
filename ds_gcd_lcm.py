def gcd(a,b):
    while b:
        r=a%b
        a=b
        b=r
    return a

def lcm(a,b):
    return (a*b) // gcd(a,b)

print(gcd(12,8))
print(lcm(4,3))