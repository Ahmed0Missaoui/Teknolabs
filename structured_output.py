from langchain_groq import ChatGroq
from langchain.output_parsers import StructuredOutputParser
from dotenv import load_dotenv
import os
import json
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("Missing GROQ_API_KEY. Please set it in your environment variables.")
model = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.3,
    max_tokens=1000,
    api_key=api_key
)
response_schemas = [
    {
        "name": "plat",
        "description": "A Tunisian dish name.",
        "type": "string",
    },
    {
        "name": "description",
        "description": "Description of the Tunisian dish.",
        "type": "string",
    }
]

parser = StructuredOutputParser(response_schemas=response_schemas)
prompt = """Veuillez répondre dans le format JSON suivant :
{
    "plat": "<Nom du plat tunisien>",
    "description": "<Description du plat tunisien>"
}
Donne-moi un plat tunisien et sa description."""
try:
    response = model.invoke(prompt)
    print("Raw Response:", response.content)

    if not hasattr(response, 'content') or not response.content.strip():
        raise ValueError("Model returned an empty or invalid response.")

    try:
        data = parser.parse(response.content)
        print("✅ Résultat Structuré :")
        print(f"🍽️ Plat : {data['plat']}")
        print(f"📖 Description : {data['description']}")
    except json.JSONDecodeError as e:
        print(f"❌ JSONDecodeError: {e}")
        print("🔍 Raw Data:", response.content)

except AttributeError as e:
    print(f"❌ AttributeError: {e}")
except ValueError as e:
    print(f"❌ ValueError: {e}")
except Exception as e:
    print(f"❌ Une erreur inattendue s'est produite: {e}")
