from langchain_groq import ChatGroq
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent
from dotenv import load_dotenv
import os

load_dotenv()
cle = os.getenv("GROQ_API_KEY")
modele = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.3,
    max_tokens=500,
    api_key=cle
)

outils = load_tools(["serpapi", "llm-math"], llm=modele)
agent = initialize_agent(outils, modele, agent="-shot-react-description", verbose=True)

reponse = agent.run("Quelle est la capitale de la Tunisie ?")
print(reponse)
