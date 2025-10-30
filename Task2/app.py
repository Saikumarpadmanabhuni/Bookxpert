# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from retrieval import find_best_match
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Recipe Chatbot 🍳", description="Suggest recipes from ingredients", version="1.0")

# Enable CORS for local HTML frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RecipeRequest(BaseModel):
    ingredients: str

@app.post("/recipe")
def suggest_recipe(req: RecipeRequest):
    recipe = find_best_match(req.ingredients)
    if not recipe:
        return {"response": "❌ Sorry, I couldn't find a recipe with those ingredients."}

    # Format the output with clear bullet points and line breaks
    formatted_output = (
        f"🍽️  Title: **{ recipe['title']}**\n\n"
        f"👨‍🍳 *Ingredients:*\n"
        f"{format_ingredients(recipe['ingredients'])}\n\n"
        f"📝 *Instructions:*\n"
        f"{format_instructions(recipe['instructions'])}"
    )

    return {"response": formatted_output}


def format_ingredients(ingredients_text: str):
    # Split by comma and format neatly
    items = [i.strip() for i in ingredients_text.split(",") if i.strip()]
    return "\n".join([f"• {i}" for i in items])


def format_instructions(instructions_text: str):
    # Split sentences and make them into steps
    steps = [s.strip().capitalize() for s in instructions_text.replace('.', '.|').split('|') if s.strip()]
    return "\n".join([f"{idx+1}. {step}" for idx, step in enumerate(steps)])


# Run the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
