# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
from main import Main
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def input():
    result={}
    if request.method == 'POST':
        text = request.form['text']
        main = Main(text)
        result = main.get_output()
        threshold = int(request.form["threshold"])
        order = main.get_order()
        return render_template("input.html", result=result, threshold=threshold, order=order)
    else:
        return render_template("input.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
