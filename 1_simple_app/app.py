from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html", message = "Hello World 3!")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=3000)