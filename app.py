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
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_sockets import Sockets
import asyncio
import datetime

r=[]
connected=set()

@app.route("/")
def home():
    return "E"
async def e(websocket,path):
    await websocket.send("[CLIENT]")
    connected.add(websocket)
    async for message in websocket:
        print("----")
        print(websocket)
        print(path)
        print(message)
        print("----")
        print(f"[MSG] : {message}")
        await websocket.send(f"[BACK] {message}")
        if message.startswith("[LIST] "):
            sda=message
            print(sda)
            for conn in connected:
                await conn.send(sda)
        else:
            if message=="[START]":
                print("FNWIAOFNIWAFOAWFINAWFNIOFNIOAWAWFNIOAWFNIONIOAWFAWFNIOFNIOAWNIOWFAINO")
                for conn in connected:
                    try:
                        await conn.send("[START]")
                    except Exception as e:
                        print(e)
                        print(e)
                        print(e)
                        print(e)
            else:
                if message=="[DONE]":
                    await websocket.send(str(r))
                    await websocket.send(str(r))
                    await websocket.send(str(r))
                    await websocket.send(str(r))
                    num1=min(r)
                    comwda=r
                    comwda.remove(num1)
                    num2=min(r)
                    comwda.remove(num2)
                    num3=min(r)
                    comwda.remove(num3)
                    num4=min(r)
                    comwda.remove(num4)
                    num5=min(r)
                    comwda.remove(num5)
                    xd=datetime.datetime.now()
                    xd=str(xd)
                    xd=xd.split(" ")
                    xd=xd[0]
                    new_req=Sock(date=xd,num5=num5,num4=num4,num3=num3,num2=num2,num1=num1)
                    db.session.commit()
                    await websocket.send("[SERVER] prime")
                else:
                    r.append(message)

start_server = websockets.serve(e, '0.0.0.0', os.environ['PORT'])
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(start_server).run_forever()
#asyncio.get_event_loop().run_forever()
if __name__=="__main__":
    app.run()
