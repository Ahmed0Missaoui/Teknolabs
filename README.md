Description des modules du projet

    smart_agent.py
    Implémente un agent intelligent capable de répondre à des questions simples en s'appuyant sur des outils comme SerpAPI pour la recherche web et LLM-Math pour les calculs.
    🔹 Exemple : "Quelle est la capitale de la Tunisie ?"

    rag_chain.py
    Met en œuvre une chaîne RAG (Retrieval-Augmented Generation) permettant de répondre à des questions spécifiques à partir d’un ensemble de documents.
    🔹 Chargement des documents
    🔹 Génération d’embeddings
    🔹 Indexation avec FAISS
    🔹 Recherche contextuelle d’informations

    memory_agent.py
    Développe un agent conversationnel doté de mémoire contextuelle grâce à ConversationBufferMemory.
    🔹 Suit l’historique de la conversation
    🔹 S’adapte aux informations fournies par l’utilisateur
    🔹 Exemple : Se souvient du prénom donné dans un échange précédent

    main.py
    Script principal qui montre comment utiliser les agents avec des prompts dynamiques basés sur des templates.
    🔹 Exemple : Générer une liste de plats populaires en fonction d’un type de cuisine donné

    prompts.py
    Contient les modèles de prompts utilisés dans le projet.
    🔹 Exemple de prompt : "Donne-moi {n} plats populaires de la cuisine {cuisine}."

    requirements.txt
    Spécifie les dépendances nécessaires pour faire fonctionner le projet :
    🔹 langchain
    🔹 faiss-cpu
    🔹 python-dotenv
    🔹 et d’autres bibliothèques utiles
