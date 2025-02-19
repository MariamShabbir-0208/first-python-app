from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Streamlit App Redirect</title>
            <meta http-equiv="refresh" content="0;url=https://first-python-app-mariamshabbir-0208.streamlit.app">
        </head>
        <body>
            <p>Redirecting to Streamlit Cloud...</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
