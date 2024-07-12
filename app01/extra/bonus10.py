import shutil

archive = shutil.make_archive("todo_v1", "zip", "app01/extra/todo")
print("Archive created:", archive)