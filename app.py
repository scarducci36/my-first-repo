#This is my first python file, which I am using to learn how to use Flask
#It is important to remember to use a virtual environment while coding in a multilple file project using Python
# The reason being is that so many projects are dependent on external packages and different projects may require different versions 
# To avoid version conflicts and issues, a virtual environemnts isolates the dependencies for that specific project

# python -m venv venv 
# venv\Scripts\activate
# pip install Flask

from flask import Flask 

app = Flask(__name__)

# Creating a list of possible responses for the eight ball 

responses = [
    "Yes, definately!"
    "Ask again later"
    "No way!"
    "It is certain."
    "Very doubtful."
    "Better not tell you now."
]

# Then use Python's random.choice() to pick one: 
import random

@app.route("/")
def magic_eight_ball():
    answer = random.choice(responses)
    return f"<h1>{answer}</h1>"