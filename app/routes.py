from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
	aUser = {"Username" : "Sajid"}
	posts = [{
		"Author" : {"aUsername" : "Gillian"}, 
		"body" : "Amazing day today!"},
		{"Author" : {"aUsername" : "Moustafa"}, 
		"body" : "How's everyone doing?"}]
	return render_template ("index.html",title="Home",aUser=aUser,posts=posts)

@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash("Login requested for aUser {}, aRemember_Me={}".format(form.aUsername.data, 			form.aRemember_Me.data))
		return redirect(url_for("index"))
	return render_template("login.html",title="Sign In",form=form)
