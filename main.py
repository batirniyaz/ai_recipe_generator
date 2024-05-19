from fastapi import FastAPI
from utils import generate_recipe_description_free, generate_recipe_description_premium
from model import DescriptionRequest

app = FastAPI()




@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/recipe_free_version")
async def recipe_description_free(description: DescriptionRequest):
    description = generate_recipe_description_free(description)
    return {"message": description}


@app.post("/recipe_premium_version")
async def recipe_description_premium(description: DescriptionRequest):
    description = generate_recipe_description_premium(description)
    return {"message": description}
