from flask import Flask, render_template

app = Flask(__name__)

jobs_dict = [
	{
		"id": 1,
		"title" : "Data Analyst",
		"location" : "Berlin, Germany",
		"salary" : "€80,000"
	},
	{
		"id": 2,
		"title" : "Front End Developer",
		"location" : "Munich, Germany",
		"salary" : "€40,000"
	},
	{
		"id": 3,
		"title" : "Project Manager",
		"location" : "Cologne, Germany",
		"salary" : "€150,000"
	}
]

# Web code
@app.route("/")

def hello_world():
	return render_template("index.html", jobs = jobs_dict)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)