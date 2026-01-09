from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Symptom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symptom_text = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<Symptom {self.symptom_text}>"
