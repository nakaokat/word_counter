# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
import main, test
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def input():
    result={}
    if request.method == 'POST':
        text = request.form['text']
        result = main.main(text, main.ignore)
        threshold = int(request.form["threshold"])
        return render_template("input.html", result=result, threshold=threshold)
    else:
        return render_template("input.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
