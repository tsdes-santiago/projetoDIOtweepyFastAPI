from credentials import MONGO_URI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pprint
from fastapi import FastAPI
import nest_asyncio
from pyngrok import ngrok
import uvicorn


uri = MONGO_URI 
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Carregando o banco de dados 
db = client.twitter_trends

print(db.list_collection_names())
# Carregando a coleção
collection = db.trends

pprint.pprint(collection.find_one())

def get_trends():
    data = []
    
    for trends in collection.find({}).sort('rank'):
        # Obtém os trends do banco de dados ordenados por rank
        data.append(f"rank: {trends['rank']} - {trends['topic']}")
    
    return data

app = FastAPI()

@app.get('/index')
async def home():
  return get_trends()

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
