import asyncio
import websockets
 
@asyncio.coroutine
def hello(websocket, path):
    # name = yield from websocket.recv()
    # print("< {}".format(name))
    # greeting = "Hello {}!".format(name)
    yield from websocket.send("FF")
    # yield from websocket.send(greeting)
    # print("> {}".format(greeting))
 
start_server = websockets.serve(hello, '192.168.1.151', 33332)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
