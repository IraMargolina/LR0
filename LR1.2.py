import sys

def fib(m): 
    if m <= 0:
        return 0
    f0 = 0
    f1 = 1
    for i in range(2, m + 1):
        c = f1
        f1 = f0 + f1
        f0 = c
    return f1

#Для чисел Фибоначи должно выполняться тождество Кассини, при котором алгоритм будет считаться верным
def kassini(s):
    if s < 0:
        print("Input Error")
    else:
        if fib(s)*fib(s + 2) - fib(s + 1)**2 == (-1)**(s + 1):
            print("Проверка с помощью тождества Кассини для чисел Фибоначи", s, s + 1, s + 2, "выполнена")
            print("АЛГОРИТМ ВЕРНЫЙ!")
        else:
            print("АЛГОРИТМ НЕВЕРНЫЙ")


def menu():
    print('Для нахождения числа Фибоначи нажмите 1')
    print('Для проверки алгоритма с помощью тождества Кассини нажмите 2')
    print('Для выхода нажмите 0')
    k = input()
    if k == '1': 
        l = int(input('Введите номер числа Фибоначи n '))
        print(l, "Число Фибоначи =", fib(l))
        menu()
    elif k == '2':
        p = int(input('Введите номер числа Фибоначи для проверки '))
        kassini(p)
        menu()
    elif k == '0':
        print('Спасибо!:)')
    else:
        menu()


def main():
    if len(sys.argv) == 1:
        menu()
    elif len(sys.argv) == 3:
        n_name = sys.argv[1]
        n_value = sys.argv[2]
        if n_name == "-n":
            try:
                n = int(n_value)
                print(n, "Число Фибоначи =", fib(n)) 
            except:
                print("Input Error")
                menu()
        else:
            print("Input Error")
            menu()
    else:
        print("Input Error")
        menu()


if __name__ == '__main__':
    main()
