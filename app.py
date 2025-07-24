import gradio as gr
import numpy as np
import seaborn as sns

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure the API key is set
if not os.environ.get("MISTRAL_API_KEY"):
    raise EnvironmentError("MISTRAL_API_KEY not found in environment variables.")

from langchain.chat_models import init_chat_model

# Initialize the model
model = init_chat_model("mistral-large-latest", model_provider="mistralai")

from langchain_mistralai import ChatMistralAI

llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.05,
    max_retries=2,
)


def prepare_input(weight, height, activity, age, goal, sleep_hours):
    in_weight = float(weight)
    in_height = float(height)
    in_activity = activity
    in_age = int(age)
    in_goal = goal
    in_sleep_hours = float(sleep_hours)
    
    messages = [
        (
            "system",
            "you are a veteran nutritionist who is always answers with a proper diet plan which includes portion size and time of eating and do no recommend supplimentary whey protien",
        ),
        ("human", f"My weight is {in_weight},my height is {in_height},my activity frequency is {in_activity} my age is {in_age} and my goal is {in_goal} and i sleep {in_sleep_hours}hours in a day ,give me a diet plant according to it.Also Give a breakdown of all macro and micro nutrients with calories."),
    ]
    
    ai_msg = llm.invoke(messages)
    return ai_msg.content

interface = gr.Interface(
    fn=prepare_input,
    inputs=[
        gr.Slider(0, 200, step=0.5, label="Weight in KGs "),
        gr.Slider(0, 280, step=0.5, label="Height in cms "),
        gr.Dropdown(
            ["Sedentary: little or no exercise", "Light: exercise 1-3 times/week", "Moderate: exercise 4-5 times/week","Active: daily exercise or intense exercise 3-4 times/week","Very Active: intense exercise 6-7 times/week","Extra Active: very intense exercise daily, or physical job"],
            label="Activity Frequecy", info= " "
        ),
        gr.Slider(0, 80, step=1, label="Age"),
        gr.Textbox(
            label=" Define Fitness Goal",
            lines=8,
        ),
        gr.Slider(0, 12, step=0.5, label="Sleep Hours"),
    ],
    outputs=gr.Markdown(label="Diet Plan"),
    title="Your Diet Plan",
    description="Enter Your Stats",
)

interface.launch(inline=True,share=True)