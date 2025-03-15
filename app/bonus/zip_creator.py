import zipfile

def make_archive(filepaths, dest_dir):
    with zipfile.ZipFile(dest_dir, 'w') as z:
        for filepath in filepaths:
            z.write(filepath)

if __name__ == "__main__":
    make_archive(filepaths=["bonus9.py", "zip_creator.py"], dest_dir="bonus9.zip")