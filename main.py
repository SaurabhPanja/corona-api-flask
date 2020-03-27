from corona_api import corona_data_api
from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_corona_api():
    return corona_data_api

if __name__ == '__main__':
   app.run()
