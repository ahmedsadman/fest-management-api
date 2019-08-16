from application import db


class ParticipantModel(db.Model):
    __tablename__ = 'participants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    email = db.Column(db.String(30), unique=True)
    is_leader = db.Column(db.Boolean, default=False)
    institute = db.Column(db.String(60), nullable=True)

    # for many to many relationship, maps user to participated events
    events = db.relationship('EventModel', secondary='event_participant',
                             backref=db.backref('participants', lazy='dynamic'))

    def __init__(self, name, email, is_leader=False, institute=None):
        self.name = name
        self.email = email
        self.is_leader = is_leader
        self.institute = institute

    def json(self):
        return {
            'name': self.name,
            'email': self.email,
            'institute': self.institute,
            'is_leader': self.is_leader
        }

    def save(self):
        '''save the item to database'''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
