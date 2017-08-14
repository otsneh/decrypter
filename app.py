from flask import Flask, render_template
app = Flask(__name__,  static_folder='public')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/dist/<path:filename>')
def serve_dist(filename):
    return app.send_from_directory('/dist/', filename)
