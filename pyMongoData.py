from credentials import MONGO_URI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = MONGO_URI
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Criando o banco de dados
db = client.twitter_trends
# Criando a coleção bank
collection = db.trends
print(db.trends)

dados_nosql = [
    {
      "topic": "#BBB24",
      "rank": 1,
      "description": "Especulações sobre o paredão falso",
    },
    {
      "topic": "Marília Mendonça",
      "rank": 2,
      "description": "Documentário sobre a cantora",
    },
    {
      "topic": "Copa do Mundo",
      "rank": 3,
      "description": "Amistosos da seleção brasileira",
    },
    {
      "topic": "Lula",
      "rank": 4,
      "description": "Entrevista do presidente em rede nacional",
    },
    {
      "topic": "Bolsonaro",
      "rank": 5,
      "description": "Movimento de direita se organiza",
    },
    {
      "topic": "Eleições 2024",
      "rank": 6,
      "description": "Análises do cenário político",
    },
    {
      "topic": "Economia",
      "rank": 7,
      "description": "Medidas do governo para a inflação",
    },
    {
      "topic": "Covid-19",
      "rank": 8,
      "description": "Nova variante em estudo",
    },
    {
      "topic": "Guerra na Ucrânia",
      "rank": 9,
      "description": "Negociações de paz em andamento",
    },
    {
      "topic": "Neymar",
      "rank": 10,
      "description": "Recuperação da lesão do jogador",
    },
    {
      "topic": "#TheMaskedSingerBR",
      "rank": 11,
      "description": "Adivinhações sobre os mascarados",
    },
    {
      "topic": "#Pantanal",
      "rank": 12,
      "description": "Final da novela da Globo",
    },
    {
      "topic": "#BBB23",
      "rank": 13,
      "description": "Melhores momentos do reality",
    },
    {
      "topic": "#Futebol",
      "rank": 14,
      "description": "Resultados dos campeonatos nacionais e internacionais",
    },
    {
      "topic": "#Música",
      "rank": 15,
      "description": "Lançamentos musicais da semana",
    },
    {
      "topic": "#Tecnologia",
      "rank": 16,
      "description": "Novidades do mundo tech",
    },
    {
      "topic": "#Humor",
      "rank": 17,
      "description": "Memes e piadas",
    },
    {
      "topic": "#Política",
      "rank": 18,
      "description": "Debates e notícias políticas",
    },
    {
      "topic": "#Celebridades",
      "rank": 19,
      "description": "Fofocas e notícias do mundo dos famosos",
    },
    {
      "topic": "#Séries",
      "rank": 20,
      "description": "Lançamentos e novidades do mundo das séries",
    },
    {
      "topic": "A Fazenda 15",
      "rank": 21,
      "description": "Especulações sobre o novo elenco",
    },
    {
      "topic": "The Voice Brasil",
      "rank": 22,
      "description": "Preparativos para a nova temporada",
    },
    {
      "topic": "BBB23 Memes",
      "rank": 23,
      "description": "Melhores memes do BBB23",
    },
    {
      "topic": "Bolsonaro 2026",
      "rank": 24,
      "description": "Movimentos pró-Bolsonaro para 2026",
    },
    {
      "topic": "Lula 2023",
      "rank": 25,
      "description": "Balanço dos primeiros meses de governo",
    },
    {
      "topic": "Copa do Mundo 2026",
      "rank": 26,
      "description": "Preparativos para o evento",
    },
    {
      "topic": "Fórmula 1",
      "rank": 27,
      "description": "Corrida do fim de semana",
    },
]

# Preparando para submeter os dados
data_id = collection.insert_many(dados_nosql).inserted_ids

print(data_id)