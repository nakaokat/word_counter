# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
import main

app = Flask(__name__)


@app.route('/words')
def words():
    result = ""
    threshold = 0
    for k, v in main.main(main.news, main.ignore).items():
        if v > threshold:
            result += k + " " + str(v)  + "<br>"
    return result

@app.route('/', methods=['GET','POST'])
def input():
    result={}
    if request.method == 'POST':
        text = request.form['text']
        result = main.main(text, main.ignore)
        return render_template("input.html", result=result)
    else:
        return render_template("input.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
