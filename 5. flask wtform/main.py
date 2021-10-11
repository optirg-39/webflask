from flask import Flask
from wtforms import StringField, SubmitField
from flask import (Flask, request, render_template)
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, RadioField, DateTimeField,
					 SelectField, TextAreaField, DateField)
# from flask.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = 'mysecretkey'


class Widgets(FlaskForm):
	FirstName = StringField(label="First Name")
	LastName = StringField(label="Last Name")
	rating = SelectField(label="Rate yourself in Python", choices=[
													("1","1"),
													("2","2"),
													("3","3"),
													("4", "4"),
													("5","5")])
	choice = RadioField(label="Gender", choices=[
												("male","male"),
												("female","female",)])
	comments = TextAreaField(label="Why you like python")
	submit = SubmitField(label="Submit")


@app.route("/", methods=("GET", "POST"))
def home():
    form = Widgets()
    if form.is_submitted():
    	result = request.form
    	print(result)
    	return "FORM SUBMITTED"
    return render_template("home.html", form=form)


if __name__ == "__main__":
	app.run(debug="True")

