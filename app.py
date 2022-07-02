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
db=SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"]="postgres://fjdytdbpqlotqg:0edde1d5a396977261f0428716b633b773e28bece96617dce516284ae10e6c64@ec2-3-222-74-92.compute-1.amazonaws.com:5432/dp6uugc3h8q26"
from sqlalchemy import create_engine

x=datetime.datetime.now()
x
class Sock(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    date=db.Column(db.String(255))
    num5=db.Column(db.String(255))
    num4=db.Column(db.String(255))
    num3=db.Column(db.String(255))
    num2=db.Column(db.String(255))
    num1=db.Column(db.String(255))

    
@app.route("/")
def home():
    return "E"
async def e(websocket,path):
    await websocket.send("[CLIENT]")
    async for message in websocket:
        print(f"[MSG] : {message}")
        await websocket.send(f"[BACK] {message}")
        if message=="[START]":
            await websocket.send("[START]")
        else:
            if message.startswith("email:"):
                await websocket.send(message)
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
asyncio.get_event_loop().run_until_complete(start_server)
if __name__=="__main__":
    threading.Thread(target=asyncio.get_event_loop().run_forever()).start()
    app.run()
