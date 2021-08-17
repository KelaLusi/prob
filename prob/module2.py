with open('zen', 'r') as zen:
    file_list = (zen.read()).split('\n')

for i in range(len(file_list)):
    print(file_list[len(file_list) - i - 1])
