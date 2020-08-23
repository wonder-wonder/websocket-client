import websocket
import sys
import time
import json

f = None

def on_message(ws, message):
    j_msg = json.dumps(message)
    string = ""
    string += j_msg["acc"]["x"]
    string += j_msg["acc"]["y"]
    string += j_msg["acc"]["z"]
    string += j_msg["gyro"]["x"]
    string += j_msg["gyro"]["y"]
    string += j_msg["gyro"]["z"]
    string += j_msg["mag"]["x"]
    string += j_msg["mag"]["y"]
    string += j_msg["mag"]["z"]
    string += "\n"
    f.write(string)

def on_close(ws):
    if f is None:
      return
    f.close()

def on_open(ws):
    ut = time.time()
    f = open(str(ut),'w')

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(sys.argv[1],
                              on_message = on_message,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()