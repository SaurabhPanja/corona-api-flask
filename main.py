from corona_api import corona_data_api
from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_corona_api():
    return corona_data_api

@app.route('/<string:province>')
def get_data(province):
    try:
        province_data = corona_data_api[province]
    except:
        province_data = {"message": "Invalid request. No such province found."}
    
    return province_data

if __name__ == '__main__':
   app.run()
