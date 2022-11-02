from flask import Flask
from flask import redirect,url_for

app=Flask(__name__)
#will run first when app is opened
@app.route('/')

def hello_world():
	return 'rvce.edu.in'
	app.add_url_rule('/','hello_world')
#will run when url we give /rv
@app.route('/rv')
def rvce():
	return 'RVITM SUCKS'
	app.add_url_rule('/','rvitm',rvitm)
#will run when we give /hello in url
@app.route('/hello')
def hello():
	return redirect("https://www.rvitm.edu.in/",code=302)
#will run when we give /hello/some_username
@app.route('/hello/<name>')
def hello_name(name):
	return 'Hello %s!' % name


if __name__ == '__main__':
	app.run(debug=True)
