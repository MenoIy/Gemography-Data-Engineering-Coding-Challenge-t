import  requests
import pymongo

client = pymongo.MongoClient("mongodb+srv://menoly:sakata-1@cluster0-ehtfy.gcp.mongodb.net/test?retryWrites=true&w=majority")

collection = client.theguardian
db = collection.news


news = db.find({'keywords' : 'US news'})

for new in news :
    print('title : ', new['title'])