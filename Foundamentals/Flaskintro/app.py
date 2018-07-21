# 1 Create Flask App
from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index() :
    return render_template("index.html",name="Hoa",
    image_url="https://scontent.fhan4-1.fna.fbcdn.net/v/t1.0-9/37087847_1031817703644252_3000533220354686976_n.jpg?_nc_cat=0&oh=2ea34c4a6de2b07abdd60ba60ef02b9f&oe=5BE531AD")


@app.route("/about-me")
def about_me() :
    return " toi ten la Ngo Khoa Anh"

@app.route("/ditme/<name>")
def hello(name) :
    return "Dit me " + name 

# 2 Run app
if __name__ == "__main__" :
    app.run(debug=True)