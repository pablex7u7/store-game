# inventory/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
