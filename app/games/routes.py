from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _
from app import db
from app.models import Score
from app.games import bp
from app.games.forms import LuckyPlayerRollDice
from app.games.lucky import roll_a_dice

@bp.route('/lucky', methods=['GET', 'POST'])
@login_required
def lucky():
    form = LuckyPlayerRollDice()
    score = current_user.lucky_scores().first()
    #your_number = None
    #computer_number = None
    if score is None:
        scores = Score(player=current_user)
        db.session.add(scores)
        db.session.commit()
        return redirect(url_for('games.lucky'))

    if form.is_submitted():
        your_number = roll_a_dice()
        computer_number = roll_a_dice()
        flash(_('Your number is %(your_number)s.', your_number=your_number))
        flash(_('The computer number is %(computer_number)s.', computer_number=computer_number))
        if your_number > computer_number:
            flash(_('Congratulations! You have won'))
            score.win += 1
            db.session.commit()
            return redirect(url_for('games.lucky'))
        elif your_number < computer_number:
            flash(_('Too bad! You lost this round'))
            score.lose += 1
            db.session.commit()
            return redirect(url_for('games.lucky'))
        else:
            flash(_("It's a draw!"))
            score.draw +=1
            db.session.commit()
            return redirect(url_for('games.lucky'))
    return render_template('games/lucky.html', title='Play Lucky', score=score, form=form)

@bp.route('/leaderboard', methods=['GET', 'POST'])
@login_required
def leaderboard():
    scores = Score.query.order_by(Score.win.desc(),Score.lose.asc(),Score.draw.desc())
    return render_template('games/leaderboard.html', title=_('Leaderboard'), scores=scores)