import marks as m
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def start():
    return render_template('index.html')

@app.route("/sub",methods=['POST','GET'])
def start1():
    if request.method=="POST":
        hr = request.form['hrs']
        pred = m.marks(hr)
        mk = pred
    return render_template('sub.html',al=mk)

if __name__=='__main__':
    app.run(debug=True)
    