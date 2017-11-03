"""View functions that deal with interruptions."""
from app import app, db
from datetime import datetime, time
from flask import Blueprint, redirect, url_for
from forms import InterruptionForm
from models import Interruption


vi = Blueprint('interruption', __name__)


@app.route('/add/<int:week_id>', methods=['POST'])
def add_interruption(week_id):
    """Add a interruption."""
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
