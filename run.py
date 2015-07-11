# -*- coding: utf-8 -*-
from flask import Flask
import main

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/words')
def words():
    result = ""
    for k, v in main.main(main.news, main.ignore).items():
        if v > 1:
            result += k + " " + str(v)  + "<br>"
    return result




if __name__ == "__main__":
    app.run(debug=True)
    
