from flask import Flask
from serie_tv import serie_tv_list

app = Flask(__name__)

@app.route('/')
def home():
    return "Benvenuto nell'API delle Serie TV!"

if __name__ == '__main__':
    app.run(debug=True)
