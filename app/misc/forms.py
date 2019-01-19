from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_babel import _, lazy_gettext as _l
from wtforms.validators import DataRequired

class AddNames(FlaskForm):
    name = StringField(_l('Name'), validators=[DataRequired()])
    submit = SubmitField(_('Add Name'))

class GetNames(FlaskForm):
    submit = SubmitField(_('Get A Name'))
