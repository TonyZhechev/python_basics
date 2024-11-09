filenames = ['document', 'report', 'presentation']
for index, item in enumerate(filenames):
    filenames = f'{index}-{item.capitalize()}.txt'
    print(filenames)

