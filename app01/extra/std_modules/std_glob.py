# Working with all the files in the folder

import glob

myfiles = glob.glob(r"..\files\*.txt")
print(myfiles)

print("Existing files:")
for filepath in myfiles:
    print("\nFrom", filepath)
    with open(filepath, "r") as f:
        print(f.read())