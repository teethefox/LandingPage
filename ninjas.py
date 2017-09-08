
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')

def main():
    return render_template("index.html")

@app.route('/ninjas')

def ninjas():
    return render_template("ninjas.html")

@app.route('/dojo', methods=['POST', 'GET'])

def form():
    return render_template("dojo.html")
    name = request.form['name']
    email = request.form['email']
    return redirect(url_for("/"))


app.run(debug=True)