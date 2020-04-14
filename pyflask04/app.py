#python 3.7.2

from flask import Flask, render_template,request, url_for
import pyflask04.kf
import pyflask04.cn

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='jimin')

@app.route('/kf',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form

      return render_template("kf.html", result=result,
                             sub = pyflask04.kf.sub_list,
                             ref = pyflask04.kf.ref_list)

@app.route('/cn',methods = ['POST', 'GET'])
def result1():
   if request.method == 'POST':
      result = request.form

      return render_template("cn.html", result=result,
                             sub = pyflask04.cn.sub_list)


@app.route('/info')
def info():
    return render_template('info.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
    #app.run(debug=True)