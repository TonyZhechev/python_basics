countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']
for content,filename in zip(countries, filenames):
    file = open(filename,'w')
    file.write(content)
    file.close()