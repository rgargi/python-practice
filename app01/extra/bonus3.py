# Create a simple journal

date = input("Enter date: ")
mood = input("Enter mood: ")
thoughts = input("Let your thoughts flow:\n")

with open(f"journal_{date}.txt", "w") as f:
    f.write("Mood: " + mood + "\n")
    f.write(thoughts)

print("============")
print(date)
print("============")
print("Mood:", mood)
print(thoughts)