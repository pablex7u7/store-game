# catalog/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
