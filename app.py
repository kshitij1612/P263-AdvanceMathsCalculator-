from flask import Flask, render_template, request	
import requests

app = Flask(__name__)
@app.route('/')

def main():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def math_operations():
	equation = request.form['text']
	operation = request.form['operation']
	result = 'https://newton.now.sh/api/v2//'+operation+'/'+equation
	requests.get(result).json()
	answer = request.form['result']

	return render_template("index.html", result=answer, equation=equation)