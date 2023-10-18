from flask import Flask, render_template, request
import datetime
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    products = ["iPhone","iPad","Mac","MacBook", "Apple Watch"]
    return render_template("index.html",name=name, products = products)

@app.route("/index",methods=["post"])
def post():
    name = request.args.get("name")
    products = ["iPhone","iPad","Mac","MacBook", "Apple Watch"]
    return render_template("index.html",name=name, products = products)

if __name__ == "__main__":
    app.run(port=8000, debug=True)        