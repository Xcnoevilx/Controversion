import os

from dotenv import load_dotenv
from flask import Flask, abort, render_template
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv(
    "SECRET_KEY",
    "development-only-secret"
)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "sqlite:///controversion.db"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Import models after db is initialized.
from models import Topic


@app.route("/")
def home():
    topics = Topic.query.order_by(
        Topic.created_at.desc()
    ).all()

    return render_template(
        "index.html",
        topics=topics
    )


@app.route("/topic/<slug>")
def topic_detail(slug):
    topic = Topic.query.filter_by(
        slug=slug
    ).first()

    if topic is None:
        abort(404)

    return render_template(
        "topic.html",
        topic=topic
    )


if __name__ == "__main__":
    app.run(
        debug=os.getenv("FLASK_DEBUG", "0") == "1"
    )