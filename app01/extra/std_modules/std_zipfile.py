import zipfile
import pathlib

def create_archive(filepaths, destination_dir):
    archive_path = pathlib.Path(destination_dir, "compressed.zip")
    with zipfile.ZipFile(archive_path, 'w') as archive:
        # add each file to the archive
        # created at destination directory
        for path in filepaths:
            filepath = pathlib.Path(path)
            archive.write(path, arcname=filepath.name)
            print("File at", path, "archived.")
    print("Archive created:", archive_path)

# testing
if __name__ == "__main__":
    filepaths = ["app01/extra/todo/tasks.txt", "app01/extra/todo/todo v1.py"]
    dd = "app01/extra/todo"
    create_archive(filepaths, dd)