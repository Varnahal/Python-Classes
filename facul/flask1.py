from flask import Flask,request,render_template
 
app = Flask(__name__)
app.debug = True
 
@app.route('/')
def index():
    return render_template('indice.html')

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome="Mundo"):
    return render_template('ola.html',nome_recebido = nome)


@app.route('/login',methods=['POST','GET'])
def logar():
    if request.method == 'POST':
        return "requisição post, fazer login"
    elif request.method == "GET":
        return "requisição get, mostrar tela de login"
    else:
        return "gayzão aee"
 
if __name__ == '__main__':
    app.run()