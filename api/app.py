from flask import Flask, escape, request
from flask_swagger_ui import get_swaggerui_blueprint
import requests
import json
import pymongo

app = Flask(__name__)

#connection to mongodb database,
client = pymongo.MongoClient("mongodb+srv://menoly:sakata-1@cluster0-ehtfy.gcp.mongodb.net/test?retryWrites=true&w=majority")

collection = client.theguardian

db = collection.news


#running flask

@app.route('/')

def get():
    keyword = request.args.get('keyword')
    print(keyword)
    news = db.find({'keywords' : keyword})
    response = []
    for new in news :
        new['_id'] = str(new['_id'])
        response.append(new)
    return json.dumps(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 8100)