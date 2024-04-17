import pandas as pd
from flask import Flask, render_template, request


df = pd.read_csv("final_data.csv")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_text = request.form.get("search_text")
        if search_text:
            results = df[df['clean_content'].str.contains(search_text, case=False)]['title'].tolist()
            return render_template("results.html", search_text=search_text, results=results)
        else:
            return render_template("results.html", search_text="Nothing", results=None)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)