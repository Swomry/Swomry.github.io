#This module is kind of a mess, but it's the basis of a 'download directory' script so it's ok

from glob import glob
from time import sleep
import zipfile
import os

path = 'C:/'

print("File Compression Started...\n")

sleep(1)

print("Collecting PNG Files...\n")
files = glob(path + "/**/*.png", recursive = True)

with zipfile.ZipFile("png.zip", 'w') as zip:
    for file in files:
        try:
            print(file)
            zip.write(file)
        except:
            print("Error")


print("\nPNGs Compressed, Collecting JPG Files...\n")
files = glob(path + "/**/*.jpg", recursive = True)
print("Collected, Compressing JPG File Files...\n")
with zipfile.ZipFile("jpg.zip", 'w') as zip:
    for file in files:
        try:
            print(file)
            zip.write(file)
        except:
            print("Error")


print("\nJPGs Compressed, Collecting JPEG Files...\n")
files = glob(path + "/**/*.jpeg", recursive = True)
print("Collected, Compressing JPEG File Files...\n")
with zipfile.ZipFile("jpeg.zip", 'w') as zip:
    for file in files:
        try:
            print(file)
            zip.write(file)
        except:
            print("Error")


print("\nJPEGs Compressed, Collecting GIF Files...\n")
files = glob(path + "/**/*.gif", recursive = True)
print("Collected, Compressing GIF File Files...\n")
with zipfile.ZipFile("gif.zip", 'w') as zip:
    for file in files:
        try:
            print(file)
            zip.write(file)
        except:
            print("Error")


print("\nGIFs Compressed, Collecting TIFF Files...\n")
files = glob(path + "/**/*.tiff", recursive = True)
print("Collected, Compressing TIFF File Files...\n")
with zipfile.ZipFile("tiff.zip", 'w') as zip:
    for file in files:
        try:
            print(file)
            zip.write(file)
        except:
            print("Error")
        

print("\nTIFFs Compressed, Collecting PSD Files...\n")
files = glob(path + "/**/*.psd", recursive = True)
print("Collected, Compressing PSD File Files...\n")
with zipfile.ZipFile("psd.zip", 'w') as zip:
    for file in files:
        try:
            print(file)
            zip.write(file)
        except:
            print("Error")


print("\nPSDs Compressed, Collecting PDF Files...\n")
files = glob(path + "/**/*.pdf", recursive = True)
print("Collected, Compressing PDF File Files...\n")
with zipfile.ZipFile("pdf.zip", 'w') as zip:
    for file in files:
        try:
            print(file)
            zip.write(file)
        except:
            print("Error")


print("\nPDFs Compressed, Collecting EPS Files...\n")
files = glob(path + "/**/*.eps", recursive = True)
print("Collected, Compressing EPS File Files...\n")
with zipfile.ZipFile("eps.zip", 'w') as zip:
    for file in files:
        try:
            print(file)
            zip.write(file)
        except:
            print("Error")


print("\nEPSs Compressed, Collecting AI Files...\n")
files = glob(path + "/**/*.ai", recursive = True)
print("Collected, Compressing AI File Files...\n")
with zipfile.ZipFile("ai.zip", 'w') as zip:
    for file in files:
        try:
            print(file)
            zip.write(file)
        except:
            print("Error")


print("\nAIs Compressed, Collecting INDD Files...\n")
files = glob(path + "/**/*.indd", recursive = True)
print("Collected, Compressing INDD File Files...\n")
with zipfile.ZipFile("indd.zip", 'w') as zip:
    for file in files:
        try:
            print(file)
            zip.write(file)
        except:
            print("Error")


print("\nINDDs Compressed, Collecting RAW Files...\n")
files = glob(path + "/**/*.raw", recursive = True)
print("Collected, Compressing RAW Files...\n")
with zipfile.ZipFile("raw.zip", 'w') as zip:
    for file in files:
        try:
            print(file)
            zip.w(file)
        except:
            print("Error")

print("\nRaw files Compressed, Collecting Zips Files...\n")
files = glob(path + "*.zip", recursive = False)

print(files)

#print("Collected, Compresssing zip Files...\n")
#with zipfile.ZipFile("raw.zip", 'w') as zip:
#    for file in files:
#        try:
#            print(file)
#            zip.w(file)
#        except:
#            print("Error")


