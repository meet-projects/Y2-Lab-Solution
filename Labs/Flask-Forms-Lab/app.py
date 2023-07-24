from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "siwarha"
password = "123"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		user = request.form['username']
		pword = request.form['password']
		if user == username and pword == password:
			return redirect(url_for('home'))
	else:
		return render_template('login.html')
  

@app.route('/home')
def home():
	return render_template("home.html", friends=facebook_friends)


@app.route('/friend_exists/<string:friend>', methods=['GET', 'POST'])
def friend_exists(friend):
	if friend in facebook_friends:
		check = True
	else:
		check = False
	return render_template("friend_exists.html", check=check)



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
