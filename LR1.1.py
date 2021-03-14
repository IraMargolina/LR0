a = 78
b = 24

def gcd(c, d): 
    while (c != 0 and d != 0):
        if c > d:
            c %= d
        else: d %= c
    return c + d
    
def lcm(c, d):
    m = c * d
    while (c != 0 and d != 0):
        if c > d:
            c %= d
        else: d %= c
    return m / (c + d)

print ("НОД =", gcd(a, b))
print ("НОК =", lcm(a, b))
