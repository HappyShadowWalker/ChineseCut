# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify
import sys
import os


app = Flask(__name__)

# 添加顶层路径

runpath = os.path.split(os.path.realpath(__file__))[0]
lastindex = runpath.rfind("/")
runpath = runpath[0:lastindex+1]
runpath = runpath + "HMM"
sys.path.append(runpath)

from Viterbi import *

@app.route('/shadowwalker/api/v1.0/chinesecut', methods = ['GET'])
def chinesecut():
    origintext = request.args.get('origintext')
    if origintext == None:
        return jsonify({'cuttext', ""})
    else:
        cutres = ChineseCutStr(origintext)
        print cutres
        return jsonify({'cuttext': cutres})


if __name__ == '__main__':
    #app.run(debug = True)
    oritext = u"我是一个男孩子,喜欢中国大好河山"
    cuttext = ChineseCutStr(oritext)
    print cuttext
