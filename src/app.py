from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    # return render_template('home.html')
    return "Hello world !"


@app.get("/hello")
def sayHello():
    # return render_template('home.html')
    return jsonify({"message": "hello world"})

# @app.route('/about/<username>')
# def about_page(username):
#     return f'<h1>This is an about page of {username}</h1>'
