import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from prompts import template_de_prompt
load_dotenv()
llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.3,
    max_tokens=500,
)
prompt = template_de_prompt.format(n=3, cuisine="Italian")
réponse = llm.invoke(prompt)
print("🔹 Réponse:", réponse.content)
