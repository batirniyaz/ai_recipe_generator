import openai
from food_database import food_database
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_recipe_description_free(user_input):
    messages = [{
        "role": "system",
        "content": "You are a recipe of food generator. User will provide you with the ingredients that they have. \n"
                   "Especially users will be diabetic patients, obese people, pregnant women or people who on diet. \n"
                   "You are in free version of the recipe generator. You need to generate a recipe of food looking \n "
                   f"at given database of foods and ingredients. The database: {food_database}\n"

    },
        {
            "role": "user",
            "content": f"{user_input}"
        },
        {
            "role": "system",
            "content": "When you are generating a recipe, please answer in short terms and clear."
        }
    ]

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply


def generate_recipe_description_premium(user_input):
    messages = [{
        "role": "system",
        "content": "You are a recipe of food generator. User will provide you with the ingredients that they have. \n"
                   "Especially users will be diabetic patients, obese people, pregnant women or people who on diet. \n"
                   "You are in premium version of the recipe generator. You need to generate a recipe \n"
                   "of food or meal without any limitations. \n"
                   "Just use ingredients which will provide user and try to generate a good healthy recipe. \n"
    },
        {
            "role": "user",
            "content": f"{user_input}"
        },
        {
            "role": "system",
            "content": "When you are generating a recipe, please answer in short terms and clear."
        }
    ]

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply
