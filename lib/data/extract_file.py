import zipfile
import os

def extract_zip():
    for file in os.listdir("./"):
        if file.endswith('.zip') or file.endswith('.rar'):
            os.rename(file, "extract.zip")

    with zipfile.ZipFile('extract.zip') as file:
        file.extractall('lib/data/Extracted')

    paste = os.listdir('lib/data/Extracted')[0]
    os.rename(f'lib/data/Extracted/{paste}', 'lib/data/Extracted/Exported')
    os.remove('extract.zip')

if __name__ == "__main__":
    extract_zip()