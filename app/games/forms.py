from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_babel import _

class LuckyPlayerRollDice(FlaskForm):
    submit = SubmitField(_('Roll a dice'))

class PlayBlackJack(FlaskForm):
    play = SubmitField(_('Play'))
    next_card = SubmitField(_('Next Card'))
    stop = SubmitField(_('Stop'))