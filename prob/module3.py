# сколько букв (латинского алфавита), слов и строк
# Дополнительно: выведите на экран букву, которая встречается в тексте наименьшее количество раз.
char_num = 0
word_num = 0
list_num = 0
char_dict = {}
min_char = ''

with open('zen', 'r') as zen:
    for ilist in zen:
        list_num += 1
        word_num += len(ilist.split())
        for ichar in ilist:
            if ichar in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ':
                char_num += 1
                if ichar.lower() in char_dict:
                    char_dict[ichar.lower()] += 1
                else:
                    char_dict[ichar.lower()] = 1
min_val = char_num
for key, value in char_dict.items():
    if value <= char_num:
        min_char = key
        min_val = value


print('В тексте {} букв, {} слов и {} строк. Буква {} встречается реже всего({} раз(а))'.format(char_num, word_num, list_num, min_char, min_val))









