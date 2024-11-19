filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    with open(filename, 'w') as file:
        file.write("Hello")
        file.close()
        break

filenames = ['a.txt', 'b.txt', 'c.txt']
for filename in filenames:
    with open(filename, 'r') as file:
        print(file.read())
        file.close()