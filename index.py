from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/special")
def special():
    return render_template("special.html")


if __name__ == '__main__':
    app.run(debug=True,port=7020)
