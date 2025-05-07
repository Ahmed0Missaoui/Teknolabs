from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferMemory
from langchain.agents.agent_types import AgentType
from langchain_community.tools import DuckDuckGoSearchRun
modele = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    groq_api_key="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"
)
recherche = DuckDuckGoSearchRun()
outils = [
    Tool(
        name="Recherche Internet",
        func=recherche.run,
        description="Recherche des informations en ligne avec DuckDuckGo"
    )
]
memoire = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
agent = initialize_agent(
    tools=outils,
    llm=modele,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    memory=memoire,
    handle_parsing_errors=True
)
if __name__ == "__main__":
    resultat_1 = agent.invoke({"input": "Je m'appelle Ahmed."})
    print("🤖 Réponse 1 :", resultat_1["output"])
    resultat_2 = agent.invoke({"input": "Quel est mon prénom ?"})
    print("🤖 Réponse 2 :", resultat_2["output"])
