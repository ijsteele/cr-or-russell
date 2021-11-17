from flask import Flask
from flask import render_template

app = Flask('cr_russell')

@app.route('/')
def hello():
    return render_template("template.html")

if __name__ == "__main__":
    app.run()