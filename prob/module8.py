import os

path = 'C:\\Users\\lusha\\PycharmProjects\\prob\\prob'
file1 = 'text.txt'
file2 = 'analysis.txt'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alpha_dict = {}
percent_alpha_dict = {}
text_len = 0

with open(os.path.join(path, file1), 'r') as text:
    for icher in text.read():
        icher = icher.lower()
        if icher in alpha_dict:
            alpha_dict[icher] += 1
            text_len += 1
        elif icher == '\n' or icher == ' ':
            continue
        else:
            alpha_dict[icher] = 1
            text_len += 1


with open(os.path.join(path, file2), 'w') as text2:
    for key, value in alpha_dict.items():
        text2.write(key + ' ' + str(round((value / text_len), 3)) + '\n')
        # percent_alpha_dict[key] = round((value / text_len), 3)

with open(os.path.join(path, file2), 'r') as text2:
    print(text2.read())