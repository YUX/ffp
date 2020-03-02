# -*- coding: utf-8 -*-
from flask import Flask, Response, abort, send_from_directory
from mimetypes import MimeTypes
import requests, os

app = Flask(__name__)
app.debug = True
CHUNK_SIZE = 2048

@app.route('/<path:url>')
def proxy(url):
    r = requests.get(url, stream=True)
    
    if r.status_code != 200:
        abort(r.status_code)

    mime = MimeTypes()
    mime_type = mime.guess_type(url)
    def generate():
        for chunk in r.iter_content(CHUNK_SIZE):
            yield chunk
    return Response(generate(), mimetype=mime_type[0])


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run()
