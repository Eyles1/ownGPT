from flask import Flask, render_template, send_file
import os


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

def add_assets(directory):
    for file in os.scandir(directory):
        if file.name == "index.html":
            continue
        elif file.is_dir():
            add_assets(file.path())
        elif file.is_file():
            site_path = os.path.join("/assets" if "assets" in file.path() else "/", file.name)
            app.route(site_path)(lambda: send_file(file.path))

add_assets(os.path.join(os.getcwd(), "templates/"))

if __name__ == "__main__":
    app.run()