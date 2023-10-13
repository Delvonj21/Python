from flask import Flask, render_template, session, redirect, request
import random
import datetime

app = Flask(__name__)

app.secret_key = "its just a game"


@app.route('/')
def index():
  if 'gold' not in session:
    session['gold'] = 0
  if 'activities' not in session:
    session['activities'] = []
  return render_template("index.html", gold=session['gold'], activities=session['activities'])

@app.route('/process_money', methods=['POST'])
def process_money():
  if request.form.get('property') == "farm":
    earned = random.randrange(10,20)
    session['gold'] += earned
    


  if request.form.get('property') == "cave":
    earned = random.randrange(5,10)
    session['gold'] += earned

  if request.form.get('property') == "house":
    earned = random.randrange(2,5)
    session['gold'] += earned

  if request.form.get('property') == "casino":
    earned = random.randrange(-50,50)
    session['gold'] += earned
    
  return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
  session.clear()
  return redirect('/')
  
if __name__ == "__main__":
  app.run(debug=True)