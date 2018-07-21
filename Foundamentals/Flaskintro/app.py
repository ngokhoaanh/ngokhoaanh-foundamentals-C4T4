# 1 Create Flask App
from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index() :
    return "Hello C4T4, this is the homepage"


@app.route("/about-me")
def about_me() :
    return " toi ten la Ngo Khoa Anh"

@app.route("/ditme/<name>")
def hello(name) :
    return "Dit me " + name 

# 2 Run app
if __name__ == "__main__" :
    app.run(debug=True)