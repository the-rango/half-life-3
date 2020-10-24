from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
  return "Hello world"

@app.route("/about")
def about():
  return "We are volunteers."

@app.route("/mirror/<ncode>")
def mirror(ncode):
  return "Welcome " + ncode

@app.route("/schedule/<month>")
def sched(month):
  # code to fetch data from the db
  if month == "december":
    month = "Unavailable"
  return render_template("schedule.html", month=month)

if __name__ == "__main__":
  app.run("0.0.0.0")

