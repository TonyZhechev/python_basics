file = open("essay.txt", "r")
content = file.read()
file.close()

print(content.title())