# Agile-Web-Development-Project - Crypto College

An interactive website for learning about cryptocurrency through lessons and assesments.

## Description

This web application was created as part of a project for the CITS3403 unit at The University of Western Australia. It aims to provide an interactive learning experience on the topic of cryptocurrencies in which users can test their learning and compare it with others. Users may register or login to begin learning on the website and select lessons from a range of 5 topics, the blockchain, NFTs, crypto-mining, cryptocurrencies and the uses of cryptocurrencies. Upon logging in, the topics will be available to select at the learn page. After selecting a topic, users will be given a short video and summary notes to learn from. On completion, a three question quiz will be taken and a feedback of results will be given. These results may be visible on the world leaderboard for the website.

## Getting Started

Setup a python virtual environment:
`python3 -m venv virtual-environment`

Activate the python virtual environment:
`$source virtual-environment/bin/activate`

To run the app:
`$flask run`
- The app.py file should be in the same folder as your virtual environment folder
- Project files are provided but can also be cloned from here

To stop the app:
`$^C`

To exit the environment:
`$deactivate`

## Prerequisites

Requires:

- python3
- flask
- venv
- flask_sqlalchemy
- flask_migrate
- flask-login
- flask-wtf
- email_validator
- requests
- selenium (for testing)

## Installing

Install [python3](https://www.python.org/downloads/)

1. Set up environment

- use pip or another package manager to install virtualenv package `$ pip install virtualenv`
- create the environment `$ python3 -m venv venv`
- activate the environment `$ . venv/bin/activate`

2. Install prerequisites

- use pip to install flask package `$ pip install flask`
- use pip to install flask_sqlalchemy package `$ pip install flask_sqlalchemy`
- use pip to install flask_migrate package `$ pip install flask_migrate`
- use pip to install flask-login package `$ pip install flask-login`
- use pip to install flask-wtf package `$ pip install flask-wtf`
- use pip to install email_validator package `$ pip install email_validator`
- use pip to install requests package `$ pip install requests`
- use pip to install selenium package (if you want to run selenium tests) `$ pip install selenium`


3. `flask run`

This should start the app running on localhost at port 5000

## Deployment

via local host

## Built With

Vscode and git

## Testing

- To run unit tests, within your virtual environment `$ python tests.py`
- For selenium testing, chrome webdriver must be installed and configured https://sites.google.com/a/chromium.org/chromedriver/home
- You can then run with `$ python testing-sele.py`

## Authors

- Bhasura Samarasekara Vitharana Gamage (22616672)
- Brandon Ke (22731448)
- Kshitiz Singh (22627009)
- William Knight (21722128)

## References

- Crypto College Logo (including favicon): https://www.flaticon.com/download/icon/landing/70035?format=png&size=512
- Blockchain png: https://rubygarage.org/blog/how-blockchain-works
- NFT png: https://en.wikipedia.org/wiki/Non-fungible_token
- Crypto Mining png: https://www.iconfinder.com/icons/3329018/bitcoin_bitcoin_mining_mine_mining_icon
- Ethereum png: https://en.wikipedia.org/wiki/Ethereum
- Bitcoin png (including Broken Bitcoin): http://www.pngall.com/bitcoin-png/download/24844
- Code Background: https://www.devonblog.com/continuous-delivery/code-analysis-service-sonarcloud/
- Patrick png: https://www.pinterest.com.au/pin/587227238891101162/?d=t&mt=login

- Live Bitcoin Prices: https://coinlib.io/widgets
- CoinGecko
