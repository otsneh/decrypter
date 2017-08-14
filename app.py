from flask import Flask, render_template
app = Flask(__name__,  template_folder='public')

@app.route('/')
def home():
    return render_template('index.html')
