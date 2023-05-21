"""
    'r' - Открывает файл на чтение. (Значение по умолчанию)
    'w' - Открывает файл на запись. Если файла нет, то будет создан новый.
          Если файл существует, данные в нем будут перезаписаны.
    'x' - Открывает файл на запись. Если файл уже существует, операция завершится ошибкой.
    'a' - Открывает файл и дозаписывает в него данные, не стирая предыдущие. 
          Создает новый файл, если он не существует.
    't' - Открывает файл как текстовый. (Значение по умолчанию)
    'b' - Открывает файл в бинарном/двоичном режиме.
    '+' - Позволяет работать с файлом как для записи так и для чтения.
"""

# file = open(file='hello.txt', mode='r')
# print(file.name)
# print(file.mode)
# print(file.read())
# file.close()

# with open(file='hello.txt') as file:
#     # print(file.read(8))
#     # print(file.readline())
#     # print(file.readlines())

#     # for line in file.readlines():
#     #     print(line.strip())

#     for line in file:
#         print(line.strip())

# my_str = 'Hack The Planet'
# my_str_2 = 2
# passwords_list = ['qwerty', '12345', 'xxxxxx', 'I was here', 'TEST', '45435435']

# with open(file='secret_file.txt', mode='a') as file:
#     # file.write(str(my_str_2))

#     # for passwd in passwords_list:
#     #     file.write(f'{passwd}\n')

#     file.writelines([line+'\n' for line in passwords_list])

import requests

response = requests.get('https://assets.reedpopcdn.com/cyberpunk_hacker_A3GLQcj.jpg/BROK/resize/1920x1920%3E/format/jpg/quality/80/cyberpunk_hacker_A3GLQcj.jpg')

with open(file='cyberpunk2.jpg', mode='wb') as file:
    file.write(response.content)


