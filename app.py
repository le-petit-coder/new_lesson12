import logging

from flask import Flask, request, render_template, send_from_directory
from main.main import main_web
from loader.loader import loader_bp

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_web)
app.register_blueprint(loader_bp)

logging.basicConfig(filename='basic.log', level=logging.INFO)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()