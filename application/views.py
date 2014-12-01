from application import application
from flask import Blueprint, render_template, abort, request, redirect, url_for
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
	try:
		return render_template('%s.html' % page)
	except TemplateNotFound:
		abort(404)

@simple_page.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'darknawg63' or request.form['password'] != 'password':
			error = "Dude! Looks like you fucked up :)"
		else:
			return redirect(url_for('.show'))
	return render_template('login.html', error=error)