from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Recipe(BaseModel):
    id: int
    name: str
    ingredients: list[str]
    instructions: str
    created_at: datetime = datetime.now()

app = FastAPI(summary="Mini recipes API")

#In memory storage
recipes_db: list[Recipe] = []

@app.get("/")
async def root():
    return {"message": "Welcome to the Mini Recipes API"}

@app.get("/api/recipes", response_model=list[Recipe])
async def get_recipes():
   return recipes_db

@app.get("/api/recipes/{recipe_id}", response_model=Recipe)
async def get_recipe(recipe_id: int):
    for recipe in recipes_db:
        if recipe.id == recipe_id:
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")

@app.post("/api/recipes", response_model=Recipe)
async def create_recipe(recipe: Recipe):
    recipes_db.append(recipe)
    return recipe

@app.delete("/api/recipes/{recipe_id}")
async def delete_recipe(recipe_id: int):
   for i, recipe in enumerate(recipes_db):
        if recipe.id == recipe_id:
            recipes_db.pop(i)
            return {"detail": "Recipe deleted"}
   raise HTTPException(status_code=404, detail="Recipe not found")
