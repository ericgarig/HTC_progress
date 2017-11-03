"""Views of the app."""
from app import app, db

from datetime import date, datetime, time, timedelta

from flask import redirect, render_template, url_for

from forms import GoalForm, InterruptionForm, ReviewForm, TaskForm

from models import Goal, Interruption, Review, Tasks, Week


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


@app.route('/add_interruption/<int:week_id>', methods=['POST'])
def add_interruption(week_id):
    """Add a goal task."""
    f = InterruptionForm()
    print(f.data)
    if f.validate_on_submit():
        dt = datetime.combine(f.date.data, time.min)
        new_interruption = Interruption(week_id=week_id,
                                        inter_date=dt,
                                        person=f.person.data,
                                        reason=f.reason.data)
        print(new_interruption)
        db.session.add(new_interruption)
        db.session.commit()
    else:
        print('validation failed')
    return redirect(url_for('worksheet', week_id=week_id))


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


@app.route('/debug')
@app.route('/debug/<week_id>')
def debug_data(week_id=None):
    """Display data for given week."""
    goals = Goal.query.all()
    interruptions = Interruption.query.all()
    weeks = Week.query.all()
    tasks = Tasks.query.all()
    return render_template('debug.html',
                           goals=goals,
                           interruptions=interruptions,
                           weeks=weeks,
                           tasks=tasks)
