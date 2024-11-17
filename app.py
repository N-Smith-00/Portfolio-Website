from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)