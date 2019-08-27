from sqlalchemy import func
from application import db
from datetime import datetime


class ParticipantModel(db.Model):
    __tablename__ = 'participants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    email = db.Column(db.String(30), unique=True)
    institute = db.Column(db.String(60), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)

    # for many to many relationship, maps user to events/teams
    events = db.relationship('EventModel', secondary='event_participant', lazy='dynamic',
                             backref=db.backref('participants', lazy='dynamic'))
    teams = db.relationship('TeamModel', secondary='team_participant', lazy='dynamic',
                            backref=db.backref('team_members', lazy='dynamic'))

    def __init__(self, name, email, institute=None):
        self.name = name
        self.email = email
        self.institute = institute

    def save(self):
        '''save the item to database'''
        db.session.add(self)
        db.session.commit()

    def has_participated_event(self, event_id):
        return self.events.filter_by(id=event_id).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find(cls, _filter):
        '''find participants by given filter'''
        query = cls.query
        for attr, value in _filter.items():
            query = query.filter(func.lower(
                getattr(cls, attr)) == func.lower(value))
        return query.all()
