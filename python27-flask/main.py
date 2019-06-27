#!/usr/bin/env python
# -*- coding: utf-8 -*-

   
from google.appengine.api import urlfetch
import json
from flask import Flask, render_template, request
import train_service

app = Flask(__name__)
app.debug = True


networkJson = urlfetch.fetch("https://tokyo.fantasy-transit.appspot.com/net?format=json").content  # ウェブサイトから電車の線路情報をJSON形式でダウンロードする
network = json.loads(networkJson.decode('utf-8')) # JSONとしてパースする（stringからdictのlistに変換する）

@app.route('/')
# / のリクエスト（例えば http://localhost:8080/ ）をこの関数で処理する。
# ここでメニューを表示をしているだけです。
def root():
  return render_template('hello.html')

@app.route('/pata')
# /pata のリクエスト（例えば http://localhost:8080/pata ）をこの関数で処理する。
# これをパタトクカシーーを処理するようにしています。
def pata():
  # とりあえずAとBをつなぐだけで返事を作っていますけど、パタタコカシーーになるように自分で直してください！
  #pata = request.args.get('a', '') + request.args.get('b', '')
  pata1 = request.args.get('a')
  pata2 = request.args.get('b')
  pata = ''
  i = 0
  if (pata1 or pata2) == None:
    return render_template('pata.html', pata='No input')
  if len(pata1) <= len(pata2):
    while i < len(pata1):
      pata += pata1[i]
      pata += pata2[i]
      i += 1
    while i < len(pata2):
      pata += pata2[i]
      i += 1
  else:
    while i < len(pata2):
      pata += pata1[i]
      pata += pata2[i]
      i += 1
    while i < len(pata1):
      pata += pata1[i]
      i += 1          
    
  # pata.htmlのテンプレートの内容を埋め込んで、返事を返す。
  return render_template('pata.html', pata=pata)

@app.route('/norikae')
# /norikae のリクエスト（例えば http://localhost:8080/norikae ）をこの関数で処理する。
# ここで乗り換え案内をするように編集してください。
def norikae():
  answer = 'hello'
  start = request.args.get('start')
  end = request.args.get('end')
  graph = train_service.create_graph(network)
  ans_list = train_service.search_shortest_paths_bfs(graph, start, end)
  path = train_service.create_line_station_list(ans_list, network)
  answer = train_service.choose_line(path)

  return render_template('norikae.html', network=network, answer = answer)

