# 🔍 Name Matching System (BERT + FAISS)

This project is a **Name Matching System** that finds the most similar names from a dataset when a user inputs a name.  
It uses **Sentence Transformers (MiniLM)** for generating embeddings and **FAISS** for efficient similarity search.

---

## 📂 Project Structure

📁 name-matching/
│  
├── name_matcher.py        # Main Python script  
├── names.txt              # Dataset of names (one per line)  
├── requirements.txt       # Python dependencies  
└── README.md              # Documentation  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/name-matching.git
cd name-matching

2️⃣ Create and Activate Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate   # On macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Project
python name_matcher.py


You’ll see a prompt like this:

---------------------------------------------
 Enter a name to search (or type 'exit' to quit):


Type any name (e.g., Geetha) and hit Enter.

🧠 Example Input & Output
Input
Enter a name to search (or type 'exit' to quit): Geta

Output
Best Match:
   Uma  (Similarity: 0.554)

Similar Matches:
1. Uma                        Score: 0.554
2. Suma                       Score: 0.545
3. Sita                       Score: 0.480
4. Deepa                      Score: 0.476
5. Komala                     Score: 0.423
6. Kavitha                    Score: 0.401
7. Sunita                     Score: 0.398
8. Shobha                     Score: 0.385
9. Rekha                      Score: 0.380
10. Sarita                    Score: 0.378

🧩 How It Works

Loads all names from names.txt.

Normalizes text (removes special characters, converts to lowercase, handles Unicode).

Encodes names using Sentence Transformer model all-MiniLM-L6-v2.

Builds a FAISS index for fast similarity lookup.

Searches for top-k most similar names and displays similarity scores.

---

🧰 Requirements

Python 3.8+
SentenceTransformers
FAISS
Numpy
Unidecode
