import code
from flask import Flask, render_template, redirect, request, url_for, session
import json

app = Flask("movie recommendation")

movies={}

movies=code.set_movies("movies.csv")
print(movies)

@app.route("/") # converts normal function to view function
def homepage(): # view function
    print("Someone is at the homepage", flush=True)
    return render_template("index.html", input1=movies)

@app.route("/post_path")
def getResults():
    values=response.json
    


if __name__ == "__main__":
    app.run('127.0.0.1', port=5500)
