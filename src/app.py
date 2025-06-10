import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, render_template_string

def mensaje():
    return "¡Universidad Tecnológica!"

app = Flask(__name__)

@app.route("/")
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Integración Continua 2025</title>
        <style>
            body {
                background-color: #1e1e2f;
                color: #ffffff;
                font-family: Helvetica, sans-serif;
                text-align: center;
                margin-top: 50px;
            }
            h1 {
                color: #00b894;
            }
            button {
                font-size: 16px;
                padding: 10px 20px;
                margin-top: 20px;
                background-color: #00b894;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #00cec9;
            }
        </style>
    </head>
    <body>
        <h1>¡Bienvenido, Marcelo!</h1>
        <form action="/mostrar" method="get">
            <button type="submit"> Presionar </button>
        </form>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route("/mostrar")
def mostrar():
    msg = mensaje() 
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Integración Continua 2025</title>
        <style>
            body {{
                background-color: #1e1e2f;
                color: #ffffff;
                font-family: Helvetica, sans-serif;
                text-align: center;
                margin-top: 50px;
            }}
            h1 {{
                color: #00b894;
            }}
            img {{
                margin-top: 20px;
                border: 3px solid #00b894;
                border-radius: 10px;
            }}
        </style>
    </head>
    <body>
        <h1>{msg}</h1>
        <img src="{{{{ url_for('static', filename='utn.png') }}}}" width="300" alt="Logo UTN">
        <br><br>
        <a href="/" style="color:#00b894;">Volver</a>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
