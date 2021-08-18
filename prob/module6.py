import os

text = 'text.txt'
cipher = 'cipher_text.txt'
path = 'C:\\Users\\lusha\\PycharmProjects\\prob\\prob'

with open(os.path.join(path, text), 'r') as file:
    # print('Содержимое файла {}:'.format(text))
    shift = 0
    for iline in file:
        # print(iline)
        shift += 1
        with open(os.path.join(path, cipher), 'a') as ciph:
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            word = ''
            for icher in iline:
                if icher.isupper():
                    i = (alphabet.find(icher.lower()) + shift) % len(alphabet)
                    word += alphabet[i].upper()
                else:
                    i = (alphabet.find(icher) + shift) % len(alphabet)
                    word += alphabet[i]
            ciph.write(word)
            ciph.write('\n')

with open(os.path.join(path, cipher), 'r') as ciph:
    for iline in ciph:
        print(iline)