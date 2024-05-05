from flask import Flask , render_template




app = Flask((__name__))


@app.route('/')
def main():
    name = 'NOAHOrtikov'
    tutor = 'diaper baby'
    return render_template('main.html',name = name,tutor = tutor,age = 99)





app.run(debug=True)