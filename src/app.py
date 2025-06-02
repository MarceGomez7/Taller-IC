from flask import Flask, render_template_string, url_for
from src.logic import mensaje

app = Flask(__name__)

@app.route("/")
def index():
    # Usamos el mensaje de la lógica
    msg = mensaje()
    
    # HTML básico con el mensaje y la imagen
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
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
