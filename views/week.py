"""View functions that deal with goals."""
from app import app, db
from datetime import date, datetime, time, timedelta
from flask import Blueprint, redirect, url_for
from models import Review, Week


vw = Blueprint('week', __name__)


@app.route('/week/new')
def week_new():
    """Route for adding a new week.

    Creates a week week for the Monday of this week.
    """
    today = datetime.combine(date.today(), time.min)
    this_sunday = (today - timedelta(days=today.isoweekday() % 7))

    if Week.query.filter_by(week=this_sunday).first() is None:
        new_week = Week(week=this_sunday)
        db.session.add(new_week)
        db.session.commit()
    week_id = Week.query.filter_by(week=this_sunday).first().id

    for i in range(5):
        reveiw_dt = this_sunday + timedelta(days=(i + 1))
        new_review = Review(week_id=week_id, review_day=reveiw_dt)
        db.session.add(new_review)
    db.session.commit()

    return redirect(url_for('worksheet', week_id=week_id))
