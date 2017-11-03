"""View functions that deal with goals."""
from app import app, db
from flask import Blueprint, redirect, url_for
from forms import GoalForm
from models import Goal


vg = Blueprint('goal', __name__)


@app.route('/add_goal/<int:week_id>', methods=['POST'])
def add_goal(week_id):
    """Add a goal task."""
    f = GoalForm()
    print(f.data)
    if f.validate_on_submit():
        new_goal = Goal()
        f.populate_obj(new_goal)
        new_goal.week_id = week_id
        db.session.add(new_goal)
        db.session.commit()
    else:
        print('validation failed')
    return redirect(url_for('worksheet', week_id=week_id))
