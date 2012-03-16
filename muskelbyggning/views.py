from muskelbyggning import app
from flask import render_template

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/blogs/")
def blogs():
	return render_template("blogs.html")

@app.route("/post/<int:post_id>")
def show_post(post_id):
	return render_template("show_post.html", post_id=post_id)
