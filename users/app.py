# users/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/users')
def users():
    return render_template('users.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
