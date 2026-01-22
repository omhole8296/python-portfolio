from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField ,IntegerField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-movies-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500),  nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()


class Update(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5')
    ranking = IntegerField('Your Ranking Out of 10')
    review = StringField('New review')
    submit=SubmitField('Done') 

class Add(FlaskForm):
    title = StringField('Movie Title',validators=[DataRequired()])
    submit=SubmitField('Add Movie') 


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = Add()
    if add_form.validate_on_submit():
        # movie_title = request.args.get('title')  it is por get an below is for post
        movie_title = add_form.title.data  
        response = requests.get("https://api.themoviedb.org/3/search/movie", params={"api_key":API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
        # return redirect(url_for('home'))
    return render_template("add.html",form=add_form)



@app.route("/edit", methods=["GET", "POST"])
def edit():
    update_form = Update()
    movie_id = request.args.get('id')
    if update_form.validate_on_submit():
    # if request.method == "POST":
        movie_to_update = db.get_or_404(Movie, movie_id)
        movie_to_update.rating = request.form["rating"]
        movie_to_update.ranking = request.form["ranking"]
        movie_to_update.review = request.form["review"]
        db.session.commit()
        return redirect(url_for('home'))
    movie_selected = db.get_or_404(Movie, movie_id)
    return render_template("edit.html", movie=movie_selected,form=update_form)


@app.route('/delete')
def delete():
        movie_id = request.args.get('id')
        movie_to_delete = db.get_or_404(Movie, movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()    
        return redirect(url_for('home'))


@app.route('/add/select')
def select():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key":API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/original{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit",id=new_movie.id))
    
if __name__ == '__main__':
    app.run(debug=True)
      