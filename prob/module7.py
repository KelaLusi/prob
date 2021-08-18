import os

firts_file = 'first_tour.txt'
sec_file = 'second_tour.txt'
needful_scores = 0
path = 'C:\\Users\\lusha\\PycharmProjects\\prob\\prob'

with open(os.path.join(path, sec_file), 'w') as file2:
    with open(os.path.join(path, firts_file), 'r') as file1:
        print('Содержимое файла {}:'.format(firts_file))
        for iline in file1:
            print(iline)
            iline_list = iline.split()
            if len(iline_list) == 1:
                needful_scores = int(iline)
            else:
                if int(iline_list[2]) >= needful_scores:
                    file2.write(iline_list[1][0].upper() + '. ' +  iline_list[0] + ' ' + iline_list[2] + '\n')

with open(os.path.join(path, sec_file), 'r') as file2:
    print('\nСодержимое файла {}:'.format(sec_file))
    for iline2 in file2:
        print(iline2)
