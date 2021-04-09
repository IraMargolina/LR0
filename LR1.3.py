import sys
import random
import argparse


def gen_file(size, symbols, line, word):

    def sym(s):
        if s == '1':
            return random.randrange(48, 58)
        if s == '3':
            return random.choice(list(range(1040, 1104)) + [1105, 1025])
        if s == '4':
            h = random.randrange(31, 65535)
            if chr(h).isprintable():
                return h
            else:            
                h = sym(4)
        return random.choice(list(range(65, 91)) + list(range(97, 123)))

    my_path = input('Введите путь к файлу: ')
    try:
        f = open(my_path + '\\text.txt', 'w', encoding = 'utf-8') 
    except:
        f = open('text.txt', 'w', encoding = 'utf-8') 
        print('Неверный путь. Файл открыт в текущем каталоге')

    if type(line) == int:
        cur_line = line
    if type(word) == int:
        cur_word = word

    switch = input('Если хотите отключить отображение статуса генерирования, нажмите 1 ')

    while(f.tell() < size):
        if type(line) == tuple: 
            cur_line = random.randrange(line[0], line[1] + 1)
        for i in range(cur_line):
            if f.tell() < size:
                if type(word) == tuple: 
                    cur_word = random.randrange(word[0], word[1] + 1)
                for j in range(cur_word):
                    if f.tell() < size:
                        print(chr(sym(symbols)), end = '', file = f)
                        if switch != '1':
                            print(round(f.tell()/size*100, 0), end = '')
                            print('\r', end = '')
                f.write(' ')
        f.write('\n')
    f.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--my_size', '-msi', type = int, help = 'Введите размер файла')
    parser.add_argument('--my_symbols', '-msy', type = int, help = 'Выберите разрешённые символы (1 - digits, 2 - latin, 3 - cyrillic, 4 - utf-8): ')
    parser.add_argument('--my_line', '-ml', help = 'Введите количество слов в строке (точно или диапазон через запятую): ')
    parser.add_argument('--my_word', '-mw', help = 'Введите длину слова (точно или диапазон через запятую): ')
    my_namespase = parser.parse_args()
    if my_namespase.my_size is None:
        my_size = input('Введите размер файла: ')
    else:
        my_size = my_namespase.my_size
    try:
        my_size = int(my_size)
    except:
        print('Ошибка ввода')
        sys.exit()

    if my_namespase.my_symbols is None:
        my_symbols = input('Выберите разрешённые символы (1 - digits, 2 - latin, 3 - cyrillic, 4 - utf-8): ')
    else:
        my_symbols = my_namespase.my_symbols
    if my_symbols != '1' and my_symbols != '2' and my_symbols != '3' and my_symbols != '4':
        print('По умолчанию выводятся символы latin')

    if my_namespase.my_line is None:
        my_line = input('Введите количество слов в строке (точно или диапазон через запятую): ')
    else:
        my_line = my_namespase.my_line
    my_line = tuple(my_line.split(','))
    try:
        if len(my_line) == 1 and my_line[0] != '':
            my_line = int(my_line[0])
        elif len(my_line) == 2:
            my_line = tuple(int(i) for i in my_line)
        else:
            my_line = (10, 50)
            print('По умолчанию (10, 50)')
    except:
        print('Ошибка ввода')
        sys.exit()

    if my_namespase.my_word is None:
        my_word = input('Введите длину слова (точно или диапазон через запятую): ')
    else:
        my_word = my_namespase.my_word
    my_word = tuple(my_word.split(','))
    try:
        if len(my_word) == 1 and my_word[0] != '':
            my_word = int(my_word[0])
        elif len(my_word) == 2:
            my_word = tuple(int(i) for i in my_word)
        else:
            my_word = (5, 9)
            print('По умолчанию (5, 9)')
    except:
        print('Ошибка ввода')
        sys.exit()

    gen_file(my_size, my_symbols, my_line, my_word)


if __name__ == "__main__":
    main()
