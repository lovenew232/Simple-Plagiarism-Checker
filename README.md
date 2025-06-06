# Simple Plagiarism Checker

A simple web application built with Flask that computes a basic cosine similarity score to compare user-entered text against a reference database. This project showcases how to create a minimal plagiarism detection tool using only Python's built-in capabilities, without relying on external machine learning libraries. The app uses Flask to handle web requests and Jinja2 templates for displaying results in the browser.
---

## Table of Contents

- [Key Highlights](#key-highlights)
- [System Requirements](#system-requirements)
- [Setup Instructions](#setup-instructions)
- [Directory Layout](#directory-layout)
- [Using It](#using-it)
- [How this program works](#how-this-program-works)
- [Extending and Customizing](#extending-and-customizing)

---

## Key Highlights

- A straightforward web form for inputting or pasting text.  
- Calculates cosine similarity percentage against a single baseline text file (`plag_database.txt`).  
- Shows a “match percentage” with a responsive circular progress indicator and a results card displayed only after submitting.  
- Clean and minimal styling with a gradient background and centered content card.  
- Uses only Python’s built-in libraries and Flask—no external NLP or ML packages required.

---

## System Requirements

- Python version 3.7 or higher  
- Python package installer `pip`

Install Flask via:

```bash
pip install Flask
```

---

## Setup Instructions

1. **Clone or downlaod this repository**:

   ```bash
   git clone <your-repository-URL>
   cd <repository-folder>
   ```

2. **Create and activate a virtual environment (recommended)**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install Flask** (if you haven’t already):

   ```bash
   pip install Flask
   ```

4. **Verify that your folder structure looks like this**:

   ```
   Simple-Plagiarism-Checker/
   ├── plag_database.txt
   ├── plagiarism.py
   ├── req.txt  # (optional) if you pin Flask version
   ├── static/
   │   └── style.css
   └── templates/
       └── plag_web.html
   ```

---

## Directory Layout

```
Simple-Plagiarism-Checker/
│
├── static/                      # CSS, JS, images (served at /static/…)
│   └── style.css                # Main stylesheet for layout & colors
│
├── templates/                   # Flask/Jinja2 templates
│   └── plag_web.html            # HTML form + result display
│
├── plag_database.txt            # Reference text file for “database” comparison
│
├── plagiarism.py                # Flask application & cosine-similarity logic
│
└── req.txt (optional)
```

- **`plagiarism.py`**

  - Implements two Flask routes:

    - `GET /` → renders `plag_web.html` with empty fields.
    - `POST /` → reads `query` from the form, tokenizes and lowercases it, reads `plag_database.txt`, builds word counts, computes cosine similarity, and re-renders `plag_web.html` with `query` and `output`.

- **`templates/plag_web.html`**

  - Contains Jinja2 placeholders (`{{ query }}`, `{{ output }}`) and a link to `{{ url_for('static', filename='style.css') }}`.

- **`static/style.css`**

  - Defines a gradient background, fonts, button styles, container styling, and result formatting.

---

## Using It

1. **Run the Flask app**:

   ```bash
   python plag.py
   ```

2. **Open a web browser** and go to:

   ```
   http://127.0.0.1:5000
   ```

3. **Paste or type your text** into the “Input Text” textarea.

4. Click **“Check Plagiarism”**.

5. The page will reload (styled exactly the same), displaying:

   - Your original text (still in the textarea).
   - Below, a line like:

     ```
     Input query text matches 42.37% with the database.
     ```

---

## How this program works

1. **Tokenization**

   - Converts both user input and the database1.txt content to lowercase.
   - Removes punctuation and splits on whitespace using a regex (re.sub(r"[^\w]", " ", text).split()), producing word lists.

2. **Vocabulary Building**

   - Merges the user and database word lists into a combined list of unique tokens (universalSetOfUniqueWords).

3. **Term-Frequency Vectors**

   - For each unique token, we count how many times it appears in the user’s word list (`queryTF`) and how many times it appears in the database’s word list (`databaseTF`).
   - That produces two equal-length integer vectors, each of length = “number of unique words.”

4. **Cosine-Similarity Calculation**

   - **Dot product** = sum of element-wise products (e.g., `sum(queryTF[i] * databaseTF[i] for i in range(n))`).
   - **Magnitude** of each vector = square root of the sum of squares of its elements (e.g., `math.sqrt(sum(q*q for q in queryTF))`).
   - **Cosine similarity** = `(dot_product) / (||queryTF|| * ||databaseTF||)`. Multiplying by 100 yields a percentage. If either vector has magnitude 0 (i.e., empty input or empty database), we output `0.00%` to avoid division by zero.

5. **Rendering the Result**

   - We build a string, e.g.

     ```
     Input query text matches 73.45% with the database.
     ```

   - Then we call:

     ```python
     return render_template("plag_web.html", query=inputQuery, output=output)
     ```

     so that Jinja2 injects the user’s original text back into the `<textarea>` and displays the `output` inside an `<h3>`.

---

## Extending and Customizing

- **Compare against multiple reference files**

  - Instead of reading a single `plag_database.txt`, we can iterate over several database files and show similarity scores for each.

- **Use TF-IDF instead of raw counts**

  - Replace term frequencies with TF-IDF vectors for improved accuracy, leveraging libraries like scikit-learn.

- **Add Stopword Removal & Text Normalization**

  - For more accurate results, integrate NLP libraries (e.g., NLTK, SpaCy) to remove common words and reduce words to their base form.

- **Implement Dynamic Updates with AJAX**

  - Use JavaScript (Fetch/XHR) to send the user’s text to a `/check` endpoint and update the match percentage dynamically without reloading the whole page.

- **Support File Uploads**

  - Add a second form input (`<input type="file" …>`) so users can upload different files of different formats like `.txt`, `.pdf` etc. to read and process its contents server-side.

- **Upgrade UI wtih CSS Frameworks**

  - Replace custom styles with Bootstrap, Tailwind, or similar frameworks for a more refined user interface.

---


Built with ❤️ by \[LOVENEW YADAV] — a simple Flask example demonstrating cosine similarity-based plagiarism detection.
