"""Forms."""
from flask_wtf import FlaskForm

from wtforms import BooleanField, DateField, IntegerField, StringField

from wtforms.validators import DataRequired, Optional


class TaskForm(FlaskForm):
    """Form for entering tasks."""

    prep_dev = StringField('Development', render_kw={"placeholder":
                           "New research/development to do"})
    prep_doc = StringField('Documentation', render_kw={"placeholder":
                           "New cleanup/documentation to do"})
    review_dev = StringField('Development', render_kw={"placeholder":
                             "Research/Development done"})
    review_task = StringField('Task', render_kw={"placeholder":
                              "Project/Task done"})
    review_doc = StringField('Documentation', render_kw={"placeholder":
                             "Cleanup/Documentation done"})

    def validate(self):
        """Overridden validate method."""
        if not super(TaskForm, self).validate():
            return False
        if not self.prep_dev.data and \
           not self.prep_doc.data and \
           not self.review_dev.data and \
           not self.review_task.data and \
           not self.review_doc.data:
            return False
        return True


class GoalForm(FlaskForm):
    """Form for entering goals."""

    goal = StringField('Goal', validators=[DataRequired()], render_kw={
                       "placeholder": "Goal for the week"})
    priority = IntegerField('Priority',
                            validators=[DataRequired()],
                            render_kw={
                                "placeholder": "Specify priority ( 1-5 )"})
    pct_done = IntegerField('Pct Done', validators=[Optional()], render_kw={
                            "placeholder": "Percentage done ( 1-100 )"})
    weeks_pushed = IntegerField('Weeks Pushed',
                                validators=[Optional()],
                                render_kw={
                                    "placeholder": "# weeks already pushed"})


class InterruptionForm(FlaskForm):
    """Form for entering interruptions."""

    date = DateField('Date', validators=[DataRequired()], render_kw={
                     "placeholder": "Specify a date"})
    person = StringField('Person', validators=[DataRequired()], render_kw={
                         "placeholder": "Who interrupted/met you"})
    reason = StringField('Reason', validators=[DataRequired()], render_kw={
                         "placeholder": "Why the interruption/meeting"})


class ReviewForm(FlaskForm):
    """Form for entering daily review."""

    date = DateField('Date', validators=[DataRequired()], render_kw={
                     "placeholder": "Specify a date"})
    planning = BooleanField('Daily Planning')
    dev = BooleanField('Personal Dev / Training')
    tickets = BooleanField('Ticket Management')
    cleanup = BooleanField('Cleanup / Documentation')
    review = BooleanField('Daily Task Review')
    goals = BooleanField('Set and Check weekly goals ( Mon/Fri )')
