from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/somar/')
@app.route('/somar/<n1>/<n2>')
def somar(n1=0,n2=0):
    res = float(n1)+float(n2)
    return str(res)


if __name__ == '__main__':
    app.run()