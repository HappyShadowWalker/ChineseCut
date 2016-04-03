# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/shadowwalker/api/v1.0/chinesecut', methods = ['GET'])
def chinesecut():
    origintext = request.args.get('origintext')
    if origintext == None:
        return jsonify({'cuttext', ""})
    else:
        return jsonify({'cuttext':"这是切分好的句子"})


if __name__ == '__main__':
    app.run(debug = True)
