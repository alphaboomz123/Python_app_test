import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return """
    <!doctype html>
    <html lang="th">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>BMS Flask Starter</title>
    </head>
    <body style="font-family:Arial,sans-serif;max-width:760px;margin:60px auto;padding:0 20px;">
        <h1>BMS Flask Starter</h1>
        <p>Python / Flask application is running.</p>
        <p>Health check: <code>/health</code></p>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return jsonify(status="ok", app="bms-flask-starter", runtime="python-flask"), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
