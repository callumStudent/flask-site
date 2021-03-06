from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/programming')
def programming():
    return render_template('programming.html')

@app.route('/japanese')
def japanese():
    return render_template('japanese.html')
    
@app.route('/archery')
def archery():
    return render_template('archery.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.secret_key = "\x02d\xe1\x9aOU\xac\xe1\x06\xfe\xc3f\xf8\x94\x11uBD>\xce\x95\xb5-\x05"
    app.debug = True
    app.run()
