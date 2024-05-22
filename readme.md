# LAB GDG LeMans "Viens coder ton chatbot pour analyser un document avec un LLM"

🐍  approche python...

## description 

* un frontend pour l'UI du chatbot
* un backend pour la gestion des documents et le llms

utilisation du cloud Groq https://console.groq.com/ pour exécuter le LLM

## installation 

### documents à prendre en compte

ajouter les documents à indexer dans le répertoire data

### backend 

```bash
$ cd backend

# creation env virtuel
$ python3 -m venv venv-llms
$ source venv-llms/bin/activate

# installation des modules python 
$ pip install groq langchain langchain-core langchain-groq langchain-together langchain-community sentence_transformers chromadb pypdf unstructured
```

compléter les API TOKEN dans le fichier config.py

```bash
# démarrage du serveur
$ python3 server.py
```

tester avec le playground http://localhost:5000/playground/

### frontend 

```bash
$ cd frontend

# installation des modules js 
$ npm install
```

```bash
# démarrage du front
$ npm start
```

tester avec http://localhost:3000


## lab 

### étape 1

à partir de https://python.langchain.com/v0.2/docs/integrations/chat/groq/

compéter le fichier chain.py dans le répertoire backend-etape1

* penser à compléter config.py
* tester avec server.py


### étape 2

à partir de https://python.langchain.com/v0.2/docs/integrations/vectorstores/chroma/#passing-a-chroma-client-into-langchain et https://docs.together.ai/docs/embeddings-python

compéter le fichier chain.py dans le répertoire backend-etape2

* penser à compléter config.py
* tester avec ?

### étape 3

à partir de https://python.langchain.com/v0.2/docs/tutorials/retrievers/#installation et https://python.langchain.com/v0.2/docs/integrations/chat/groq/


compéter le fichier chain.py dans le répertoire backend-etape2

* penser à compléter config.py
* tester avec server.py
