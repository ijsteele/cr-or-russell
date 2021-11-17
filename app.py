from flask import Flask
from flask import render_template

app = Flask('cr_russell')

@app.route('/')
def home():
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run()
#testing