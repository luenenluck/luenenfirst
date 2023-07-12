from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index.html')
def index(): # put application's code here
    return render_template('index.html')

@app.route('/about.html')
def about(): # put application's code here
    return render_template('about.html')

@app.route('/lizu.html')
def lizu(): # put application's code here
    return render_template('lizu.html')

@app.route('/lisuzu.html')
def lisuzu(): # put application's code here
    return render_template('lisuzu.html')

@app.route('/fengjing.html')
def fengjing(): # put application's code here
    return render_template('fengjing.html')

if __name__ == '__main__':
    app.run()
