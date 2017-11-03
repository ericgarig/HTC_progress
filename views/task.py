"""View functions that deal with tasks."""
from app import app, db
from flask import Blueprint, redirect, url_for
from forms import TaskForm
from models import Tasks


vt = Blueprint('task', __name__)


@app.route('/add_task/<int:week_id>', methods=['POST'])
def add_task(week_id):
    """Add a new task."""
    f = TaskForm()
    print(f.data)
    if f.validate_on_submit():
        new_task = Tasks()
        f.populate_obj(new_task)
        new_task.week_id = week_id
        db.session.add(new_task)
        db.session.commit()
    else:
        print('validation failed')
    return redirect(url_for('worksheet', week_id=week_id))
