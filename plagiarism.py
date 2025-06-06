from flask import Flask, request, render_template
import re, math

app = Flask(__name__)

@app.route("/", methods=["GET"])
def loadPage():
    return render_template("plag_web.html", query="", output="", percentage=0)

@app.route("/", methods=["POST"])
def cosineSimilarity():
    try:
        inputQuery = request.form.get("query", "").strip()
        lowercaseQuery = inputQuery.lower()

        # Build universal vocabulary
        queryWordList = re.sub(r"[^\w]", " ", lowercaseQuery).split()
        databaseText = open("plag_database.txt", "r").read().lower()
        databaseWordList = re.sub(r"[^\w]", " ", databaseText).split()

        universalSetOfUniqueWords = []
        for w in queryWordList + databaseWordList:
            if w and (w not in universalSetOfUniqueWords):
                universalSetOfUniqueWords.append(w)

        # Build TF vectors
        queryTF = [ queryWordList.count(word) for word in universalSetOfUniqueWords ]
        databaseTF = [ databaseWordList.count(word) for word in universalSetOfUniqueWords ]

        # Dot product & magnitudes
        dotProduct = sum(q * d for q, d in zip(queryTF, databaseTF))
        qMagnitude = math.sqrt(sum(q * q for q in queryTF))
        dMagnitude = math.sqrt(sum(d * d for d in databaseTF))

        if qMagnitude == 0 or dMagnitude == 0:
            matchPercentage = 0.0
        else:
            matchPercentage = (dotProduct / (qMagnitude * dMagnitude)) * 100.0

        output = f"Input query text matches {matchPercentage:.2f}% with the database"
        return render_template(
            "plag_web.html",
            query=inputQuery,
            output=output,
            percentage=matchPercentage
        )

    except Exception:
        output = "Please enter valid data."
        return render_template(
            "plag_web.html",
            query=inputQuery,
            output=output,
            percentage=0
        )

if __name__ == "__main__":
    app.run(debug=True)
