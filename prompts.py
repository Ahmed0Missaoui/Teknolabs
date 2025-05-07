from langchain.prompts import PromptTemplate
template_de_prompt = PromptTemplate.from_template(
    "Donne-moi {n} plats populaires de la cuisine {cuisine}."
)
