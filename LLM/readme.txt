ollama ps
ollama stop llama3.2
ollama run llama3.2

tracking is done using langsmith
ollama model used downloaded on local system so no cost
can check cost of per token of openai using langsmith

API for Deployment...

swager ui 
langserve
                                                   ------> llama2 
web app     ---------> API's --------------> Route ------> openai
mobile app                                         ------> claude
                                                   ------> etc

client.py contains webapp or mobile app

for tracking of env file, if cached then use
git rm .env --cached
git add .
git commit -m "message"
git push origin main



load source --> load --> Transform(chunks) --> Embed(openAi embeddings) --> vector store 

query --> embed --> similarity search --> vector store --> Retrive most similar


using retriver (backbone is vector store)

load source --> load --> Transform(chunks) --> Embed(openAi embeddings) --> vector store 

promopts --> Chain and Retriver (using LLM models). (stuff_document_chain)

user --> retriver --> vectorstore
                  --> LLM model --> promopt

                 (using stuff document chain)