"""Debug view of the app."""
from flask import Blueprint, render_template
from models import Goal, Interruption, Tasks, Week


v_debug = Blueprint('debug', __name__)


@v_debug.route('/debug')
@v_debug.route('/debug/<week_id>')
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
