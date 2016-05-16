# -*- coding: utf-8 -*-
from flask import Flask, Response, redirect, abort
import requests
import re

app = Flask(__name__)
app.debug = False
CHUNK_SIZE = 2048

def qWhiteList(url):
    if re.match(r'ww[0-9]\.sinaimg.cn\/', url):
        site = "sinaimg"
    elif re.match(r'p[0-9]\.music.126.net\/', url):
        site = "163music"
    else:
         abort(403)
    return site

@app.route('/<path:url>')
def proxy(url):
    site = qWhiteList(url)
    if site == "sinaimg":
        r = requests.get("http://"+url, stream=True)
    elif site == "163music":
        r = requests.get("http://"+url, headers={"Referer": "http://music.163.com/"}, stream=True)
    def generate():
        for chunk in r.iter_content(CHUNK_SIZE):
            yield chunk
    return Response(generate(), headers = r.raw.headers.items())

@app.errorhandler(403)
def forbidden(e):
	return redirect("https://yux.io")

@app.errorhandler(404)
def page_not_found(e):
	return redirect("https://yux.io")

@app.errorhandler(500)
def internal_server_rror(e):
	return redirect("https://yux.io")

if __name__ == '__main__':
    app.run()
