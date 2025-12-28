from flask import Flask,request,render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("myth_chat.html")
app.run(port=8000)