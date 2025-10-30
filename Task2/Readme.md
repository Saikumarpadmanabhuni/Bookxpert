# 🍳 Recipe Chatbot 

The **Recipe Chatbot** is an intelligent conversational system that suggests recipes based on ingredients you have.  
It uses **FastAPI** as the backend and a **retrieval-based model** to find the most relevant recipes from a cleaned dataset.

---

## 📂 Project Structure

📦 recipe-chatbot/  
│  
├── app.py                        # FastAPI backend for recipe suggestions  
├── retrieval.py                  # Ingredient-based recipe retrieval logic  
├── index.html                    # Frontend chat UI  
├── requirements.txt              # Python dependencies  
└── data/  
&emsp; └── cleaned/  
&emsp;&emsp; └── recipes_2k_clean.jsonl    # Recipe dataset (required)  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/recipe-chatbot.git
cd recipe-chatbot

2️⃣ Create and Activate Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate   # On macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Make Sure Dataset Exists
Ensure the dataset file is available at:
data/cleaned/recipes_2k_clean.jsonl
If not, add it manually — this file is required for the chatbot to function.

▶️ Run the Project
Start FastAPI Server
uvicorn app:app --reload
You’ll see something like:
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
Open your browser and go to:
http://127.0.0.1:8000
Open the index.html

🧠 Example Interaction

User Input:
egg, onion, tomato

Chatbot Response:
🍽️  Title: Tomato Omelette

👨‍🍳 Ingredients:
• Egg
• Onion
• Tomato
• Salt

📝 Instructions:
1. Beat eggs.
2. Add chopped tomato and onion.
3. Cook on a hot pan with oil.
4. Serve warm.

🧩 How It Works
Frontend (index.html) — simple chat interface for user interaction.

Backend (app.py) — FastAPI handles chat requests and responses.

Retrieval Module (retrieval.py) — uses cosine similarity / vector search to find recipes matching the given ingredients.

Dataset (recipes_2k_clean.jsonl) — contains pre-cleaned recipe titles, ingredients, and instructions.

🧰 Requirements
Python 3.8+
FastAPI
Uvicorn
Pandas
Numpy
Scikit-learn
