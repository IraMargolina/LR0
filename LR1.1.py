def gcd(c, d):
    c = abs(c)
    d = abs(d)
    while c != 0 and d != 0:
        if c > d:
            c %= d
        else:
            d %= c
    return c + d
    
def lcm(c, d):
    if c == 0 and d == 0:
        return 0
    c = abs(c)
    d = abs(d)
    m = c * d
    return m // gcd(c, d)

def main():
    a = input("Введите число a ")
    b = input("Введите число b ")
   
    try:
        a = int(a)
        b = int(b)
        print("НОД =", gcd(a, b))
        print("НОК =", lcm(a, b))
    except:
        print("Input Error")
    
if __name__ == "__main__":
    main()
