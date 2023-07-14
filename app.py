from flask import Flask, render_template, send_file, request, Response
from ownGPT import ownGPT
import sys
import os


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

class Send_File:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.__name__ = self.filepath
    
    def __call__(self):
        return send_file(self.filepath)

def add_assets(directory):
    for file in os.scandir(directory):
        if file.name == "index.html":
            continue
        elif file.is_dir():
            add_assets(file.path)
        elif file.is_file():
            site_path = os.path.join("/assets" if "assets" in file.path else "/", file.name)
            app.route(site_path)(Send_File(file.path))

add_assets(os.path.join(os.getcwd(), "templates/"))


class LazyModel:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self._model = None
    
    @property
    def model(self):
        if self._model is None:
            self._model = ownGPT(self.model_name)
        return self._model

@app.route("/answer", methods = ["POST"])
def answer():
    return Response(model.model.generate(**request.json), mimetype="text/txt")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        model = LazyModel(" ".join(sys.argv[1:]))
    else:
        model = LazyModel("orca-mini-3b.ggmlv3.q4_0.bin")
    app.run()