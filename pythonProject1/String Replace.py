from dataclasses import replace

language = "Vityoria"
language = language.replace('t','k',1)
language = language.replace('y','t',1)
print(language)