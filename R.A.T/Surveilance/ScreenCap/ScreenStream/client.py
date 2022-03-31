from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient(input('Ngrok Ip: '), int(input('Ngrok Port: ')))

t = threading.Thread(target=sender.start_stream)
t.start()

while input("") != 'STOP':
    continue
sender.stop_stream()