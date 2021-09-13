from flask import Flask, render_template
from pymongo import MongoClient
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)
client = MongoClient('mongodb://test:test@localhost', 27017)

db = client.dbmovietalk
@app.route("/")
def index():
    return render_template("allinone.html")

@app.route('/aboutUs') #页面链接该路由名称
def f_infor():
    return render_template('aboutUs.html')

if __name__ == '__main__':
    app.run()

