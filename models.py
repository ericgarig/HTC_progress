"""db models."""
from app import db
# from datetime import timedelta


class Week(db.Model):
    """Week model.

    Every other class uses this as a foreign key.
    """

    id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.DateTime, nullable=False)
    tasks = db.relationship('Tasks', backref='week', lazy='dynamic')
    goals = db.relationship('Goal', backref='week', lazy='dynamic')
    interruptions = db.relationship('Interruption',
                                    backref='week', lazy='dynamic')
    review = db.relationship('Review', backref='week', lazy='dynamic')

    def __init__(self, week=None):
        """Init object."""
        self.week = week

    def __repr__(self):
        """Repr the object."""
        return '<Week {}>'.format(self.get_week_date())

    def get_week_date(self):
        """Display a human friendly date."""
        return self.week.date()


class Tasks(db.Model):
    """Task model.

    Can be for either weekly preparation of weekly review.
    """

    id = db.Column(db.Integer, primary_key=True)
    week_id = db.Column(db.Integer, db.ForeignKey('week.id'))
    prep_dev = db.Column(db.Text)
    prep_doc = db.Column(db.Text)
    review_dev = db.Column(db.Text)
    review_task = db.Column(db.Text)
    review_doc = db.Column(db.Text)

    def __init__(self, week_id=None,
                 prep_dev=None, prep_doc=None,
                 review_dev=None, review_task=None, review_doc=None
                 ):
        """Init object."""
        self.week_id = week_id
        self.prep_dev = prep_dev
        self.prep_doc = prep_doc
        self.review_dev = review_dev
        self.review_task = review_task
        self.review_doc = review_doc

    def __repr__(self):
        """Repr the object."""
        return '<Task: {}>'.format(self.week_id)


class Goal(db.Model):
    """Goal model.

    Goal field is something that should be done this week.
    """

    id = db.Column(db.Integer, primary_key=True)
    week_id = db.Column(db.Integer, db.ForeignKey('week.id'))
    goal = db.Column(db.Text, nullable=False)
    priority = db.Column(db.Integer)
    pct_done = db.Column(db.Integer)
    weeks_pushed = db.Column(db.Integer)

    def __init__(self, week_id=None,
                 goal=None,
                 priority=None,
                 pct_done=None,
                 weeks_pushed=None
                 ):
        """Init object."""
        self.week_id = week_id
        self.goal = goal
        self.priority = priority
        self.pct_done = pct_done
        self.weeks_pushed = weeks_pushed

    def __repr__(self):
        """Repr the object."""
        return '<Goal: {}>'.format(self.goal)


class Interruption(db.Model):
    """Interruption model.

    One record is an interruption of some sort.
    """

    id = db.Column(db.Integer, primary_key=True)
    week_id = db.Column(db.Integer, db.ForeignKey('week.id'))
    inter_date = db.Column(db.DateTime, nullable=False)
    person = db.Column(db.String(80))
    reason = db.Column(db.Text)

    def __init__(self, week_id=None,
                 inter_date=None,
                 person=None,
                 reason=None):
        """Init object."""
        self.week_id = week_id
        self.inter_date = inter_date
        self.person = person
        self.reason = reason

    def __repr__(self):
        """Repr the object."""
        return '<Interruption: {} on {}>'.format(self.person,
                                                 self.get_interruption_date())

    def get_interruption_date(self):
        """Display a human friendly date."""
        return self.inter_date.date()


class Review(db.Model):
    """Review model.

    Records are for a specific date, and can be one or more flags.
    """

    id = db.Column(db.Integer, primary_key=True)
    week_id = db.Column(db.Integer, db.ForeignKey('week.id'))
    review_day = db.Column(db.DateTime, nullable=False)
    planning = db.Column(db.Boolean)
    dev = db.Column(db.Boolean)
    tickets = db.Column(db.Boolean)
    cleanup = db.Column(db.Boolean)
    review = db.Column(db.Boolean)
    goals = db.Column(db.Boolean)

    def __init__(self, week_id=None,
                 review_day=None,
                 planning=None,
                 dev=None,
                 tickets=None,
                 cleanup=None,
                 review=None,
                 goals=None
                 ):
        """Init object."""
        self.week_id = week_id
        self.review_day = review_day
        self.planning = planning
        self.dev = dev
        self.tickets = tickets
        self.cleanup = cleanup
        self.review = review
        self.goals = goals

    def __repr__(self):
        """Repr the object."""
        return '<Review: {}>'.format(self.week_id)

    def get_review_date(self):
        """Display a human friendly date."""
        return self.review_day.date()
