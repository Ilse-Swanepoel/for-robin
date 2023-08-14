from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def printhelloWorld():
    html_content = "<h1>Trying some fastAPI</h1>"
    return HTMLResponse(content=html_content)

@app.get("/hello")
def printhelloWorld():
    html_content = "<h1>Hello, World</h1>"
    return HTMLResponse(content=html_content)

@app.get("/ahh")
def printAhh():
    html_content = "<h1>AAAAAAAAAAAHHHHHH!!!</h1>"
    return HTMLResponse(content=html_content)

@app.get("/slay")
def printSlay():
    html_content = "<h1>SLAY QUEEN!</h1>"
    return HTMLResponse(content=html_content)
