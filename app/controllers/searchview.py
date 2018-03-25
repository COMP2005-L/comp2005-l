from flask import render_template, flash, redirect, url_for, request, session
from app.models.User import User

@staticmethod
def search():
    form = SearchForm()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect((url_for('search_results', query=form.search.data)))
    return render_template('search.html', form=form)
