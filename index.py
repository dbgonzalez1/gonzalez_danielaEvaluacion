#importamos la libreria Flask
from flask import Flask, render_template, Request

app = Flask(__name__, template_folder='templates')



#---------------------------------------
#Ruta de pagina principal
#---------------------------------------

@app.route('/')
def iniciosesion():
    return render_template('iniciosesion.html') 

@app.route('/cliente')
def cliente():
    return render_template('cliente.html') 

@app.route('/tienda')
def tienda():
    return render_template('tienda.html') 

@app.route('/admin')
def admin():
    return render_template('admin.html') 

#---------------------------------------
#---------------------------------------

#---------------------------------------
#iniciamos la aplicacion
if __name__ == '__main__':
    app.run(debug=True)