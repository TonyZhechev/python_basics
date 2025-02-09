date =input("Enter today's date:")
mood = input("Enter today's mood rate:")
thoughts =input("Enter your thoughts:\n")

with open(f"../thoughts/{date}.txt", "w") as file:
    file.write(mood)
    file.write(thoughts)