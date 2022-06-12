# 1 -  Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет
# операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9.






# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся в
# отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста).

with open('encode.txt', 'r') as file:
    my_text = file.read()

def encode_rle(line):
    str_code = ''
    prev_char = ''
    count = 1
    for char in line:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code


str_code = encode_rle(my_text)
# print(str_code)



with open('decode.txt', 'r') as file:
    my_text2 = file.read()

def decoding_rle(line: str):
    count = ''
    str_decode = ''
    for char in line:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


str_decode = decoding_rle(my_text2)
print(str_decode)


# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в
# алфавите. ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 . Если в строку включены
# числа или специальные символы, они должны быть возвращены как есть. Также создайте функцию, которая расшифровывает эту
# строку обратно (некий начальный аналог шифрования сообщений).
# Не использовать функцию encode.

alphabet_Eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
alphabet_Rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

text = input('Enter your text: ')
key = int(input('Enter your key: '))  # на сколько симвлов смещаем шифруемый символ

def rot (alphabet_Eng, alphabet_Rus):
    result = ''
    for element in text:
        if element in alphabet_Eng:
            idex_relace = (alphabet_Eng.index(element) + key) % 26 + alphabet_Eng.index(element) // 26 * 26
            result += alphabet_Eng[idex_relace]
        elif element in alphabet_Rus:
            idex_relace = (alphabet_Rus.index(element) + key) % 33 + alphabet_Rus.index(element) // 33 * 33
            result += alphabet_Rus[idex_relace]
        else:
            result += element
    return result

print(rot(alphabet_Eng, alphabet_Rus))

