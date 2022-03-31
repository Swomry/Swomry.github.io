from vidstream import StreamingServer
from pyngrok import ngrok
import threading

PORT = 9999

receiver = StreamingServer('localhost', PORT)

ngrok.set_auth_token("26q0ieTKJTeQ67ip5XAc6QVRsOf_75TUrxQBHSKMbJzJkmpht")
ngrok.connect(PORT, 'tcp')
print(ngrok.get_tunnels())

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'STOP':
    continue
receiver.stop_server()