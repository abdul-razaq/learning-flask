from flask import Flask, render_template
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learning_flask'
db.init_app(app)
# map the root URL route to / so that when a user visits the root URL, index function
# is called and the index.html template is rendered.
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run(debug=True)