from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///controversion.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from models import Topic


@app.route("/")
def home():
    topics = Topic.query.order_by(Topic.created_at.desc()).all()
    return render_template("index.html", topics=topics)


@app.route("/topic/<slug>")
def topic_detail(slug):
    topic = Topic.query.filter_by(slug=slug).first()

    if topic is None:
        abort(404)

    return render_template("topic.html", topic=topic)


if __name__ == "__main__":
    app.run(debug=True)