from flask import Flask,render_template
app=Flask(__name__)

class Movie : 
    def __init__(self,t,c,tu) :
        self.title = t
        self.casts = c
        self.thumbnail_url = tu 

m = Movie("Batman : The darknight rises",
            "Christian Bale,Cillian Murphy",
            "https://www.sideshowtoy.com/wp-content/uploads/2017/07/dc-comics-batman-begins-batman-quarter-scale-hot-toys-feature-903127.jpg"
)
m2 = Movie("Ant man",
             "Michael Douglas. Dr. Hank Pym. Evangeline Lilly. Hope van",
             "http://www.movienewsletters.net/photos/VNM_144121R1.jpg" )

m3 = Movie("The Flash",
            "...",
            "http://static.hdonline.vn/i/resources/new/film/215x311/2017/10/10/the-flash-4.jpg?v=01")

movie_list = [m,m2,m3]

@app.route("/movie")
def index() :
    return render_template("movie.html",movies =movie_list)
   


@app.route("/casts")
def casts() :
    return render_template("casts.html",casts=["Cong Ly","Quang Teo","Xuan Bac"])

if __name__ == "__main__" :
    app.run(debug=True)
