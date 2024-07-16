filenames = ["file1.txt", "file2.txt", "file3.txt"]

for file in filenames:
    with open(f"app01/extra/files/{file}", "r") as f:
        print(file)
        print(f.read())