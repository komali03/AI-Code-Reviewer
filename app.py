import streamlit as st
import google.generativeai as genai

# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 

API_KEY = os.getenv("API_KEY")
genai.configure(api_key = API_KEY)

sys_prompt = """You are a helpful ai tutor for Coders. Coders will ask you to check their code. 
You are expected to reply with listing bugs and then giving corrected code. 
Make sure to give it correctly. In case if  student asks any questions outside the code, 
politely decline and tell them to ask the question from code corrections and suggestions on."""

model = genai.GenerativeModel(model_name = "models/gemini-1.5-flash", system_instruction = sys_prompt)
st.title("AI Code Reviewer")
user_prompt = st.text_area("Enter your code for evaluation: ")
btn_click = st.button("Validate code")
if btn_click == True:
    response = model.generate_content(user_prompt)
    st.write(response.text)
