from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/kontakti')
def kontakti():
    return "Šeit mani kontakti"

@app.route('/iepriekseja')
def iepriekseja():
    return render_template('iepriekseja.html')

if __name__ == '__main__':
    app.run(debug = True)