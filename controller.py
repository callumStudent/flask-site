from flask import Flask, request, render_template,url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = "\x02d\xe1\x9aOU\xac\xe1\x06\xfe\xc3f\xf8\x94\x11uBD>\xce\x95\xb5-\x05"
    app.debug = True
    app.run()
