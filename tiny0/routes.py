from flask import render_template, redirect, request, url_for
from tiny0 import app, db
from tiny0.forms import URLForm
from tiny0.models import URL
from tiny0.token import gen_valid_token

# Index Page
@app.route("/", methods=['GET', 'POST'])
def index():
	# Create a instance of the form
	form = URLForm()

	# If the form was valid
	if form.validate_on_submit():
		# Generate a valid token
		token = gen_valid_token()

		# Add the token and the given url to the database
		db.session.add(URL(token=token, url=form.url.data))
		db.session.commit()

		# Return the url page with the shortened url
		return render_template("url.html", url="127.0.0.1:5000/" + token)

	# If the form was invalid or not submitted
	else:
		# Return the index page with the form
		return render_template("index.html", form=form)
