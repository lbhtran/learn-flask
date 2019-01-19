from app import db
from app.misc import bp
from flask_login import login_required
from flask import render_template, flash, redirect, url_for
from flask_babel import _
from app.models import Refugees
from app.misc.forms import GetNames, AddNames

@bp.route('/add_names', methods=['GET', 'POST'])
@login_required
def add_names():
    form = AddNames()
    if form.validate_on_submit():
        name = Refugees(name=form.name.data)
        db.session.add(name)
        db.session.commit()
        flash(_('New names are added'))
        return redirect(url_for('misc.add_names'))

    names = Refugees.query.all()

    return render_template('misc/add_names.html', title='Add Names', form=form, names=names)

@bp.route('/get_names', methods=['GET', 'POST'])
@login_required
def get_names():
    form = GetNames()
    name = Refugees.query.first()
    if form.is_submitted():
        flash(_('The name is %(name)s', name=name))
        return redirect(url_for('misc.get_names'))

    return render_template('misc/get_names.html', title='Get Names', form=form, name=name)