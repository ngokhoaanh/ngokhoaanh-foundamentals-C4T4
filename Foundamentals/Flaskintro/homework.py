# exercice 1

from flask import Flask,redirect

app = Flask(__name__)
@app.route("/about-me")
def about_me() :
    return """toi ten la Khoa Anh
    18 tuoi
    thich mau xanh va yeu hoa binh
    """


    

@app.route("/school")
def school() :
    return redirect ("http://techkids.vn" ,code = 302)

if __name__ =="__main__" :
    app.run (debug=True)

# serious exercice
# exercice 1

from flask import Flask,redirect
app = Flask(__name__)
@app.route("/about-me")
def about_me() :
    return """toi ten la Khoa Anh
    18 tuoi
    thich mau xanh va yeu hoa binh
    """
@app.route("/users/<username>")
def users(username) :
    if username == "Khoaanh" :
     return redirect ("http://127.0.0.1:5000/about-me",code=303)
    else :
        return "user not found"

if __name__ == "__main__" :
    app.run(debug=True)
    