# import  requests
# import pymongo

# client = pymongo.MongoClient("mongodb+srv://menoly:sakata-1@cluster0-ehtfy.gcp.mongodb.net/test?retryWrites=true&w=majority")

# collection = client.theguardian
# db = collection.news


# news = db.find({'keywords' : 'US news'})

# for new in news :
#     print('title : ', new['title'])
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 8001)