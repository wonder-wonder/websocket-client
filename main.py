import websocket
import sys
import time
import json

f = None

def on_message(ws, message):
    j_msg = json.dumps(message)
    string = ""
    string += j_msg["sensor"]["acc"]["x"]
    string += j_msg["sensor"]["acc"]["y"]
    string += j_msg["sensor"]["acc"]["z"]
    string += j_msg["sensor"]["gyro"]["x"]
    string += j_msg["sensor"]["gyro"]["y"]
    string += j_msg["sensor"]["gyro"]["z"]
    string += j_msg["sensor"]["mag"]["x"]
    string += j_msg["sensor"]["mag"]["y"]
    string += j_msg["sensor"]["mag"]["z"]
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