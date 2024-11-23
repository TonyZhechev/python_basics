with open("story.txt", "r")as file:
    content = file.read()


with open("story_copy.txt", "w")as file:
    file.write(content)


languages = ['English', 'German', 'Spanish']
for item in languages:
    with open(f"{item}.txt", "w")as file:
            file.write(item)
