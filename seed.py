from app import app, db
from models import Topic, Claim, Evidence, Source


def seed_database():
    with app.app_context():

        db.create_all()

        if Topic.query.first():
            print("Database already contains topics.")
            return

        source = Source(
            title="Apollo 11 Mission Overview",
            author="NASA",
            publisher="NASA",
            source_type="Government record",
            url="https://www.nasa.gov/mission/apollo-11/",
            credibility_score=5,
            credibility_reasoning=(
                "Primary-source material from the agency responsible "
                "for the Apollo program."
            )
        )

        topic = Topic(
            title="Apollo 11 Moon Landing",
            slug="apollo-11-moon-landing",
            summary=(
                "Apollo 11 landed astronauts on the Moon in July 1969. "
                "Claims that the landing was staged have remained a "
                "well-known modern conspiracy theory."
            ),
            category="History",
            status="historical"
        )

        claim = Claim(
            topic=topic,
            claim_text="Apollo 11 successfully landed humans on the Moon.",
            description=(
                "The accepted historical account is that Neil Armstrong "
                "and Buzz Aldrin landed on the lunar surface while "
                "Michael Collins remained in lunar orbit."
            ),
            confidence_level=6,
            confidence_reasoning=(
                "The event is supported by extensive mission records, "
                "physical evidence, telemetry, photographs, samples, "
                "and independent observation."
            )
        )

        evidence = Evidence(
            claim=claim,
            source=source,
            title="Apollo 11 mission records",
            description=(
                "NASA maintains extensive records documenting the mission, "
                "including mission reports, photographs, communications, "
                "technical records, and lunar samples."
            ),
            evidence_type="Primary documentation",
            direction="supports",
            strength="very_strong",
            reasoning=(
                "The mission generated multiple independent categories "
                "of physical and documentary evidence."
            )
        )

        db.session.add_all([
            source,
            topic,
            claim,
            evidence
        ])

        db.session.commit()

        print("Controversion test data created.")


if __name__ == "__main__":
    seed_database()