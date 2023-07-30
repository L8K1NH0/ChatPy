# pip install python-socketio flask-socketio simple-websocket

from flask import Flask, render_template
from flask_socketio import SocketIO, send 

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# func de enviar msg
@socketio.on("message")
def gerenciar_msg(menssagem):
    send(menssagem, broadcast=True) # envia msg para todos conectados

# criar primeira pagina = primeira rota
@app.route("/") # Home page / @ = atribui uma função para oq está em baixo
def homepage(): # função
    return render_template("index.html")

# roda o aplicativo
#app.run(debug=True) # NO FINAL TIRAR MODO DEBUG
socketio.run(app, host="192.168.1.5") # digitar no terminal (ipconfig), IPv4

# Websocket -> "tunel de conexao" entre PCs

