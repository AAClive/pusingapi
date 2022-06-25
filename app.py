from flask import Flask
import socket
from flask import render_template
from flask import request
import websockets
from flask_sockets import Sockets
app=Flask(__name__)
from flask_socketio import SocketIO,send
import os
import logging
import threading
import gevent
from flask import Flask, render_template
from flask_sockets import Sockets
import asyncio
@app.route("/")
def home():
    return "E"
async def e(websocket,path):
    async for message in websocket:
        print(f"[MSG] : {message}")
        await websocket.send(f"[BACK] {message}")
start_server = websockets.serve(e, '0.0.0.0', os.environ['PORT'])
asyncio.get_event_loop().run_until_complete(start_server)
if __name__=="__main__":
    threading.Thread(target=asyncio.get_event_loop().run_forever()).start()
    app.run()
