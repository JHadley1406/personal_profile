from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def main_page():
	return render_template('main.html')
	
@app.route("/professional")
def prof_page():
	return render_template('professional.html')
	
@app.route("/personal")
def pers_page():
	return render_template('personal.html')
	
if __name__ == "__main__":
	app.run(debug=True)