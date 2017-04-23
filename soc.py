import asyncio
import websockets
import status 
import json
@asyncio.coroutine
def hello(websocket, path):
	yield from websocket.send(json.dumps(status.getStatus()))
#    name = yield from websocket.recv()
#    print("< {}".format(name))
#    greeting = "Hello {}!".format(name)
#yield from websocket.send("greeting")
#    print("> {}".format(greeting))
 
start_server = websockets.serve(hello, '192.168.1.171', 33333)
 
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
