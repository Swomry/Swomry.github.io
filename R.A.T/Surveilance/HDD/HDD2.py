import zipfile
from glob import glob

path = ""

files = glob(path, recursive = True)
print("Collected, Compressing JPEG File Files...\n")
with zipfile.ZipFile("jpeg.zip", 'w') as zip:
    for file in files:
        try:
            print(file)
            zip.write(file)
        except:
            print("Error")
