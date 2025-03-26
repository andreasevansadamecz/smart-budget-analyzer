from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd

from src.parser import load_transactions
from src.categorizer import categorize_transactions
from src.summary import show_monthly_summary
from src.visualizer import show_spending_pie_chart

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file.filename.endswith(".csv"):
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)

            df = load_transactions(file_path)
            df = categorize_transactions(df)

            show_spending_pie_chart(df, save_path="static/pie_chart.png")

            return render_template("index.html", table=df.to_html(classes="table"), chart="static/pie_chart.png")

        return "Invalid file format. Please upload a CSV."
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
