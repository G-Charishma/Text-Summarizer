from flask import Flask,request,jsonify,render_template
import google.genai as genai
client = genai.Client(api_key="AIzaSyDhTPOfuBKLxRh3DYciyAkRRuNnrpqPnSY")
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("myth_chat.html")
@app.route("/summarize",methods=["POST"])
def summarize():
    prompt=request.json["text"]
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return jsonify({"summary":response.text})
app.run(port=8000)
