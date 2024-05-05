from flask import Flask, render_template,request
import random
app = Flask(__name__)
dog_breeds={'labrador','boston terrier','Bernadoodle'}
@app.route('/')
def index():
    return render_template('index.html',breed = dog_breeds)
@app.route("/guess") 
def guess():
    return render_template("result_breeds.html")


app.run(debug=True)





