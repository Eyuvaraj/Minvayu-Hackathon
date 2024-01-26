import os
import google.generativeai as genai

GOOGLE_API_KEY = ""

with open("GOOGLE_API_KEY.txt") as f:
    GOOGLE_API_KEY = f.read()

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro")
