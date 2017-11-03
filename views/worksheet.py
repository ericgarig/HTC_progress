"""View function for the worksheet."""
from app import app
from flask import Blueprint, render_template
from forms import GoalForm, InterruptionForm, ReviewForm, TaskForm
from models import Goal, Interruption, Review, Tasks, Week


v_sheet = Blueprint('worksheet', __name__)


@app.route('/')
@app.route('/<week_id>')
def worksheet(week_id=None):
    """Main route of the one-page site."""
    week = ''
    week_list = Week.query.all()
    interruption = ''
    goals = ''
    tasks = ''
    review = ''

    task_form = TaskForm()
    goal_form = GoalForm()
    interruption_form = InterruptionForm()
    review_form = ReviewForm()

    if week_id:
        interruption = Interruption.query.filter_by(week_id=week_id).all()
        goals = Goal.query.filter_by(week_id=week_id).all()
        tasks = Tasks.query.filter_by(week_id=week_id).all()
        review = Review.query.filter_by(week_id=week_id).all()
        week = Week.query.get(week_id)
    return render_template('base.html',
                           week=week, week_list=week_list,
                           interruptions=interruption,
                           interruption_form=interruption_form,
                           goals=goals, goal_form=goal_form,
                           tasks=tasks, task_form=task_form,
                           review=review, review_form=review_form
                           )
