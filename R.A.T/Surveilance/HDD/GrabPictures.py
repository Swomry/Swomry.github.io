from glob import glob 
import zipfile

path = 'C:/Users/'

print('Collecting Png Files...')
pngs = glob(path + "/**/*.png", recursive = True)
print('Collecting Jpeg Files...')
jpgs = glob(path + "/**/*.png", recursive = True)

files = pngs+jpgs

with zipfile.ZipFile("picture.zip", 'w') as zip:
    for file in files:
        try:
            print(file)
            zip.write(file)
        except:
            print("Error")
