"""View functions that deal with goals."""
from app import db
from flask import Blueprint, redirect, url_for
from forms import GoalForm
from models import Goal


vg = Blueprint('goal', __name__)


@vg.route('/add/<int:week_id>', methods=['POST'])
def add(week_id):
    """Add a goal task."""
    f = GoalForm()
    # print(f.data)
    if f.validate_on_submit():
        new_goal = Goal()
        f.populate_obj(new_goal)
        new_goal.week_id = week_id
        db.session.add(new_goal)
        db.session.commit()
    # else:
    #     print('validation failed')
    return redirect(url_for('worksheet.worksheet', week_id=week_id))


@vg.route('/<int:goal_id>/delete')
def delete(goal_id):
    """Delete an interruption record."""
    goal = Goal.query.get(goal_id)
    week_id = goal.week_id
    db.session.delete(goal)
    db.session.commit()
    return redirect(url_for('worksheet.worksheet', week_id=week_id))


@vg.route('/<int:goal_id>/done')
def complete(goal_id):
    """Mark a goal as complete."""
    goal = Goal.query.get(goal_id)
    week_id = goal.week_id
    goal.pct_done = 100
    db.session.commit()
    return redirect(url_for('worksheet.worksheet', week_id=week_id))
