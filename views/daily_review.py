"""View functions that deal with daily reviews."""
from app import app, db
from datetime import datetime, time
from flask import Blueprint, redirect, url_for
from forms import ReviewForm
from models import Review


vd = Blueprint('daily_review', __name__)


@app.route('/add_review/<int:week_id>', methods=['POST'])
def add_review(week_id):
    """Add a daily review task."""
    f = ReviewForm()
    print(f.data)
    if f.validate_on_submit():
        review_dt = datetime.combine(f.date.data, time.min)
        rev = Review.query.filter_by(review_day=review_dt).first()
        if rev is None:
            rev = Review()
            rev.week_id = week_id
            rev.review_day = f.date.data
            db.session.add(rev)
            db.session.commit()
        rev.planning = f.planning.data if f.planning.data else rev.planning
        rev.dev = f.dev.data if f.dev.data else rev.dev
        rev.tickets = f.tickets.data if f.tickets.data else rev.tickets
        rev.cleanup = f.cleanup.data if f.cleanup.data else rev.cleanup
        rev.review = f.review.data if f.review.data else rev.review
        rev.goals = f.goals.data if f.goals.data else rev.goals
        db.session.commit()
    else:
        print('validation failed')
    return redirect(url_for('worksheet', week_id=week_id))
