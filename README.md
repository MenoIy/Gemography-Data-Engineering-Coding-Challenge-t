<a href="https://www.gemography.com/">
  <img src="https://assets.website-files.com/5e1da0fec60936a02bf7cd72/5e1da35cd91bf431ea16115a_Gemof.svg" width="300" alt="gemography logo">
</a>

[![code license](https://img.shields.io/badge/code%20license-MIT-blue.svg?longCache=true&style=for-the-badge)](https://choosealicense.com/licenses/mit/)

- [About the challenge](#about-the-challenge)
- [Requirements](#requirements)
- [Install](#Install)


## About the challenge
  The goal of this coding challenge is to create a solution that crawls for articles from a news website [THEGUARDIAN.COM], cleanses the response, stores it in a mongo database, then makes it available to search via an API.


## Technologies used
  - Flask
  - pymongo
  
### Requirements
  - python (Flask==1.1.1,requests, pymongo, dnspython)
  - Docker (for the api)
 
### Install
1. clone the project
	`git clone https://github.com/rakati/United-remote_Backend_challenge.git`
2. cd into project directory
	`cd United-remote_Backend_challenge`
3. Run scrapy (to scrap news from website)
   `scrapy crawl collector`
4. Build docker image of the API
	`docker build -t collectorapp .`
5. Run the docker container
	`docker run -it -d -p 8100:8100 collectorapp`



Now the API is working on [http://localhost:8100/](http://localhost:8100/)


## Entry points
('/') keyword=key
ex : localhost:8100/keyword=US news
