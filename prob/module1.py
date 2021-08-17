with open('numbers', 'r') as file:
    with open('answer', 'w') as file2:
        file_sum = 0
        for iline in file:
            ilist = iline.split()
            for i in ilist:
                if i.isnumeric():
                    file_sum += int(i)
        file2.write(str(file_sum))


