import websocket
import sys
import time
import json

f = None


def on_message(ws, message):
    global f
    j_msg = json.loads(message)
    string = ""
    string += str(j_msg["acceleration"]["x"]) + ","
    string += str(j_msg["acceleration"]["y"]) + ","
    string += str(j_msg["acceleration"]["z"]) + ","
    string += str(j_msg["gyro"]["x"]) + ","
    string += str(j_msg["gyro"]["y"]) + ","
    string += str(j_msg["gyro"]["z"]) + ","
    string += str(j_msg["magnetism"]["x"]) + ","
    string += str(j_msg["magnetism"]["y"]) + ","
    string += str(j_msg["magnetism"]["z"])
    string += "\n"

    if f is None:
        print("No file io")
        return
    f.write(string)


def on_close(ws):
    global f
    if f is None:
        return
    f.close()


def on_open(ws):
    global f
    ut = time.time()
    f = open(str(ut) + ".log", 'w')


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(sys.argv[1],
                                on_open=on_open,
                                on_message=on_message,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
