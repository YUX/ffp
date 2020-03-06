# -*- coding: utf-8 -*-
from flask import Flask, Response, abort, send_from_directory, redirect, request
from mimetypes import MimeTypes
import requests, os, re

app = Flask(__name__)
app.debug = False
mime = MimeTypes()
CHUNK_SIZE = 2*1024*1024

@app.route('/<path:url>')
def proxy(url):
    requestHeaders=dict(request.headers)
    #hostPattern=re.compile(r"\/\/(.*?)\/")
    #requestHost=hostPattern.findall(url)[0]
    #requestHeaders['Host']=requestHost
    try:
        requestHeaders.pop('If-None-Match')
    except:
        pass
    try:
        requestHeaders.pop('If-Modified-Since')
    except:
        pass
    try:
        requestHeaders.pop('Host')
    except:
        pass
    r = requests.get(url, stream=True,params=request.args,headers=requestHeaders)
    if r.status_code != 200:
        abort(r.status_code)
    mime_type = mime.guess_type(url)
    def generate():
        for chunk in r.iter_content(CHUNK_SIZE):
            yield chunk
    responseHeaders=dict(r.headers)
    try:
        responseHeaders.pop('Content-Encoding')
    except:
        pass
    try:
        responseHeaders.pop('Transfer-Encoding')
    except:
        pass
    return Response(generate(),headers=responseHeaders,mimetype=mime_type[0])

@app.route('/r/<path:url>')
def replace(url):
    requestHeaders=dict(request.headers)
    #hostPattern=re.compile(r"\/\/(.*?)\/")
    #requestHost=hostPattern.findall(url)[0]
    #requestHeaders['Host']=requestHost
    try:
        requestHeaders.pop('If-None-Match')
    except:
        pass
    try:
        requestHeaders.pop('If-Modified-Since')
    except:
        pass
    try:
        requestHeaders.pop('Host')
    except:
        pass
    r = requests.get(url,params=request.args,headers=requestHeaders)
    if r.status_code != 200:
        abort(r.status_code)
    mime_type = mime.guess_type(url)
    localHost=request.headers["Host"]
    pattern = re.compile(r'http(s:\/\/|:\/\/)')
    postRegex=re.sub(pattern,"https://"+localHost+"/http"+r'\1', r.text)
    responseHeaders=dict(r.headers)
    try:
        responseHeaders.pop('Content-Encoding')
    except:
        pass
    return Response(postRegex,headers=responseHeaders, mimetype=mime_type[0])

@app.route('/')
def index():
    return redirect('https://github.com/YUX-IO/ffp', code=302)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.errorhandler(500)
def internal_server_error(e):
	return redirect('https://github.com/YUX-IO/ffp', code=302)

@app.errorhandler(400)
def bad_equest(e):
	return redirect('https://github.com/YUX-IO/ffp', code=302)

if __name__ == '__main__':
    app.run()