"""View functions that deal with interruptions."""
from app import db
from datetime import datetime, time
from flask import Blueprint, redirect, url_for
from forms import InterruptionForm
from models import Interruption


vi = Blueprint('interruption', __name__)


@vi.route('/add/<int:week_id>', methods=['POST'])
def add(week_id):
    """Add a interruption."""
    f = InterruptionForm()
    # print(f.data)
    if f.validate_on_submit():
        dt = datetime.combine(f.date.data, time.min)
        new_interruption = Interruption(week_id=week_id,
                                        inter_date=dt,
                                        person=f.person.data,
                                        reason=f.reason.data)
        # print(new_interruption)
        db.session.add(new_interruption)
        db.session.commit()
    # else:
    #     print('validation failed')
    return redirect(url_for('worksheet.worksheet', week_id=week_id))


@vi.route('/<int:week_id>/<int:interruption_id>/delete')
def delete(week_id, interruption_id):
    """Delete an interruption record."""
    interruption = Interruption.query.get(interruption_id)
    week_id = interruption.week_id
    db.session.delete(interruption)
    db.session.commit()
    return redirect(url_for('worksheet.worksheet', week_id=week_id))
