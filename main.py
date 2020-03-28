from corona_api import execute
from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_corona_api():
    corona_data_api = execute()
    return corona_data_api

if __name__ == '__main__':
   app.run()
