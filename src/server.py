from pyNetSocket import *

if (ip := input("Run on (l for local): "))[0].lower() == "l":
    ip = getThisIP()
PORT = 5050

svr = Server(ip, PORT)

def send_to_all(addr, _, msg):
    sendable = f"{addr}: {msg}"
    for conn in svr.conns.values():
        svr.sendTo(conn, sendable)

print(svr.IP)

svr.onMessage(send_to_all)
svr.start()
