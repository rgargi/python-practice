import shutil

archive = shutil.make_archive("todo_v1", "zip", "../todo")
print("Archive created:", archive)