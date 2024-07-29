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

# testing archive creation
if __name__ == "__main__":
    filepaths = ["../todo/tasks.txt", "../todo/todo v1.py"]
    dd = "../todo"
    create_archive(filepaths, dd)

def extract_archive(filepaths, destination_dir):
    for path in filepaths:
        path = pathlib.Path(path)
        dest_dir = pathlib.Path(destination_dir, path.name[:-4])
        with zipfile.ZipFile(path, "r") as archive:
            archive.extractall(dest_dir)
            print("Extracted files at", path)
    print("Extracted files can be found at:", destination_dir)

# testing archive extraction
if __name__ == "__main__":
    filepaths = ["../todo/compressed.zip"]
    dd = "../todo/uncompressed"
    extract_archive(filepaths, dd)