import os

text = input('Введите строку: ')
path_list = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split()
file_name = input('Введите имя файла: ')
path = os.path.abspath(os.path.sep)

for elem in path_list:
    path = os.path.join(path, elem)

if os.path.exists(path):
    if os.path.exists(os.path.join(path, file_name)):
        answer = input('Вы действительно хотите перезаписать файл? ')
        if answer == 'да':
            with open(os.path.join(path, file_name), 'w+') as file:
                file.write(text)
        elif answer == 'нет':
            with open(os.path.join(path, file_name), 'r') as file:
                print('Содержимое файла:', file.read())
    else:
        with open(os.path.join(path, file_name), 'w+') as file:
            file.write(text)
        print('Файл успешно сохранён!')
    with open(os.path.join(path, file_name)) as file:
        print('Файл успешно сохранён!')
        print('Содержимое файла:', file.read())
print(path)






'Файл успешно сохранён!'
'Содержимое файла: '
'Вы действительно хотите перезаписать файл? ' 'да' 'нет'
'Файл успешно перезаписан!'







