from flask import Flask , render_template 
app= Flask(__name__)

class Food :
    def __init__ (self,t,d,tu):
        self.title = t
        self.des = d
        self.thumbnail_url = tu
    
f1 = Food("Pho bo",
            "ngon vai" ,
            "https://www.huongnghiepaau.com/images/nau-an/cong-thuc/pho-bo-truyen-thong-nuoc-dung-thanh-ngot.jpg")
        

f2 = Food("Bun cha",
            "ngon cuc",
            "https://images.foody.vn/res/g25/245415/prof/s576x330/foody-mobile-bc-hg-jpg-699-636245617106542261.jpg")

f3 = Food("Nem chua",
            "Ngon lanh",
            "http://www.savourydays.com/wp-content/uploads/2016/01/nem-chua.jpg" )


food_list = [f1,f2,f3]
@app.route("/food")
def index() :
    return render_template("foods.html",foods=food_list)

if __name__ == "__main__" :
    app.run(debug=True)




    

