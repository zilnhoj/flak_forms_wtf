from flask_wtf import FlaskForm
from govuk_frontend_wtf.wtforms_widgets import GovRadioInput, GovSubmitInput, GovTextInput, GovDateInput
from wtforms.fields import RadioField, SubmitField, StringField, DateField
from wtforms.validators import Email, InputRequired, Length, DataRequired

from datetime import datetime


class CookiesForm(FlaskForm):
    functional = RadioField(
        "Do you want to accept functional cookies?",
        widget=GovRadioInput(),
        validators=[InputRequired(message="Select yes if you want to accept functional cookies")],
        choices=[("no", "No"), ("yes", "Yes")],
        default="no",
    )
    analytics = RadioField(
        "Do you want to accept analytics cookies?",
        widget=GovRadioInput(),
        validators=[InputRequired(message="Select yes if you want to accept analytics cookies")],
        choices=[("no", "No"), ("yes", "Yes")],
        default="no",
    )
    save = SubmitField("Save cookie settings", widget=GovSubmitInput())

class ExampleForm(FlaskForm):

    desired_url = StringField(
        "Desired Url",
        widget=GovTextInput(),
        validators=[
            InputRequired(message="Enter an URL including the /"),
            Length(max=256, message="Must be 256 characters or fewer"),
            # Email(message="Enter an email address in the correct format, like name@example.com"),
        ],

        description="This will be used as the starting point for the DISCO data",
    )

    start_date = DateField(
                "Please enter the start date for the period you need data for",
                widget=GovDateInput(),
                validators=[
                    InputRequired(),
                    # __validate_dt
                ]
            )
    def validate_dt(form, field):
        if form.start_date.data is None:
            print(f'data in if form.data: {form.start_date.raw_data}')
            print(f'data in form.start_date.data: {form.start_date.data}')
            dt_ls = field.raw_data
            dt_str = "".join(dt_ls).strip()
            date_dt = datetime.strptime(dt_str, "%d%m%Y").date()
            data = date_dt
            form.start_date.data = date_dt
            print(f'date_dt - {date_dt}')
            print(f'form.start_date.data - {form.start_date.data}')
            return form.start_date.data
        # if not date_dt:
        #     raise ValidationError('not a valid date buddy')
        # else:
        #     print(f'in else statement {data}')
        #     # assert date_dt
        #     assert data
        print(f'form.data outside if:- {form.start_date.data}')

    submit = SubmitField("Continue", widget=GovSubmitInput())
