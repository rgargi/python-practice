filenames = ["file1.txt", "file2.txt", "file3.txt"]

for file in filenames:
    with open(f"{file}", "r") as f:
        print(file)
        print(f.read())