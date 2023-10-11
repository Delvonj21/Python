from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html",row=8,col=8,color_one='red',color_two='black')

@app.route('/<int:x>')
def row(x):
  return render_template("index.html",row=x,col=8,color_one='red',color_two='black')

@app.route('/<int:x>/<int:y>')
def col(x,y):
  return render_template("index.html",row=x,col=y,color_one='red',color_two='black')

@app.route('/<int:x>/<int:y>/<string:first>')
def col_one(x,y,first):
  return render_template("index.html",row=x,col=y,color_one=first,color_two='black')

@app.route('/<int:x>/<int:y>/<string:first>/<string:second>')
def col_two(x,y,first,second):
  return render_template("index.html",row=x,col=y,color_one=first,color_two=second)

if __name__ == "__main__":
  app.run(debug=True)