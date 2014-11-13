from app import app
from flask import render_template,request

@app.route('/')
@app.route('/index')
def index():
	return render_template('base.html')

@app.route('/',methods=['POST'])
def get_data():
	t=request.form['email']
	if t.find('@') !=-1:
		return "Thank You. We will keep in touch"
	return "error"
