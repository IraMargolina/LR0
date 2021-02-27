a = 1
b = -5
c = 6
d = b**2 - 4*a*c

if d >= 0: 
    x1 = (-b + d**(1/2))/(2*a)
    x2 = (-b - d**(1/2))/(2*a)
    print('x1 = ' + str(x1))
    print('x2 = ' + str(x2))
else: 
    print('Нет корней')
    
