file = open ("essay.txt.",'r')
content = file.read()
file.close()
n_ch = len(content)
message = f"The file contains {n_ch} characters."
print(message)