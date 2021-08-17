import os

path = 'C:\\Users\\lusha\\PycharmProjects\\prob\\prob'

def serching(path):
    TotalSize = 0
    file_num = 0
    dir_num = 0
    for elem in os.listdir(path):
        TotalSize += os.path.getsize(os.path.join(path, elem)) / 1000
        if os.path.isdir(os.path.join(path, elem)):
            dir_num += 1
            TotalSize += serching(os.path.join(path, elem))[0]
            dir_num += serching(os.path.join(path, elem))[1]
            file_num += serching(os.path.join(path, elem))[2]
        elif os.path.isfile(os.path.join(path, elem)):
            file_num += 1
    return TotalSize, dir_num, file_num

print('''Результат работы программы на примере {}:
Размер каталога (в Кб): {}
Количество подкаталогов: {}
Количество файлов: {}
      '''.format(path, serching(path)[0], serching(path)[1], serching(path)[2]))
