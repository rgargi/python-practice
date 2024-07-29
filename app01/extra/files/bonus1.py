file_contents = ["This should be in file 1", 
                 "This should be in file 2", 
                 "This should be in file 3"]
file_names = ["file1.txt", "file2.txt", "file3.txt"]

# Method 1
for index, name in enumerate(file_names):
    with open(f"{name}", "w") as f:
        f.write(file_contents[index])

# Method 2
for name, content in zip(file_names, file_contents):
    with open(f"{name}", "w") as f:
        f.write("Method 2: " + content)
