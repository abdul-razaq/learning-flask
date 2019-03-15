from flask import Flask, render_template

app = Flask(__name__)

# map the root URL route to / so that when a user visits the root URL, index function
# is called and the index.html template is rendered.
@app.route("/")
def index():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)