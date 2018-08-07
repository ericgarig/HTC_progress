"""View functions that deal with tasks."""
from app import db
from flask import Blueprint, redirect, url_for
from forms import TaskForm
from models import Tasks


vt = Blueprint('task', __name__)


@vt.route('/add/<int:week_id>', methods=['POST'])
def add(week_id):
    """Add a new task record for each task item."""
    f = TaskForm()
    # print(f.data)
    if f.validate_on_submit():
        if f.prep_dev.data:
            new_task = Tasks(week_id=week_id, prep_dev=f.prep_dev.data)
            db.session.add(new_task)
        if f.prep_doc.data:
            new_task = Tasks(week_id=week_id, prep_doc=f.prep_doc.data)
            db.session.add(new_task)
        if f.review_dev.data:
            new_task = Tasks(week_id=week_id, review_dev=f.review_dev.data)
            db.session.add(new_task)
        if f.review_task.data:
            new_task = Tasks(week_id=week_id, review_task=f.review_task.data)
            db.session.add(new_task)
        if f.review_doc.data:
            new_task = Tasks(week_id=week_id, review_doc=f.review_doc.data)
            db.session.add(new_task)
        db.session.commit()
    # else:
    #     print('validation failed')
    return redirect(url_for('worksheet.worksheet', week_id=week_id))


@vt.route('/<int:task_id>/delete')
def delete(task_id):
    """Delete an task record."""
    task = Tasks.query.get(task_id)
    week_id = task.week_id
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('worksheet.worksheet', week_id=week_id))
