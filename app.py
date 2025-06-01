from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # pour autoriser JS à appeler les routes

cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add_report", methods=["POST"])
def add_report():
    data = request.get_json()
    db.collection("reports").add(data)
    return jsonify({"status": "ok"})

@app.route("/get_reports")
def get_reports():
    reports = []
    docs = db.collection("reports").stream()
    for doc in docs:
        reports.append(doc.to_dict())
    return jsonify(reports)

if __name__ == "__main__":
    app.run(debug=True)
