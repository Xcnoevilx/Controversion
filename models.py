from datetime import datetime
from app import db


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    summary = db.Column(db.Text)
    category = db.Column(db.String(100))
    status = db.Column(db.String(50), default="active")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    claims = db.relationship(
        "Claim",
        backref="topic",
        lazy=True,
        cascade="all, delete-orphan"
    )


class Claim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(
        db.Integer,
        db.ForeignKey("topic.id"),
        nullable=False
    )
    claim_text = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    confidence_level = db.Column(db.Integer)
    confidence_reasoning = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    evidence = db.relationship(
        "Evidence",
        backref="claim",
        lazy=True,
        cascade="all, delete-orphan"
    )


class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    author = db.Column(db.String(200))
    publisher = db.Column(db.String(200))
    source_type = db.Column(db.String(100))
    url = db.Column(db.Text)
    publication_date = db.Column(db.Date)
    credibility_score = db.Column(db.Integer)
    credibility_reasoning = db.Column(db.Text)
    archived_url = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Evidence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    claim_id = db.Column(
        db.Integer,
        db.ForeignKey("claim.id"),
        nullable=False
    )
    source_id = db.Column(
        db.Integer,
        db.ForeignKey("source.id")
    )
    title = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text)
    evidence_type = db.Column(db.String(100))
    direction = db.Column(db.String(50))
    strength = db.Column(db.String(50))
    reasoning = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    source = db.relationship("Source", backref="evidence")
