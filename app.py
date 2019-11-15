from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_twitter

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/twitter_app"
mongo = PyMongo(app)

@app.route('/')
def index():
    twitter_info = mongo.db.twitter_info.find_one()
    return render_template('index.html', twitter_info = twitter_info)

# Scrape functions
@app.route('/scrape')
def scraper():
    twitter_info = mongo.db.twitter_info
    twitter_data = scrape_twitter.scrape()
    twitter_info.update({}, twitter_data, upsert = True)
    return redirect("/", code=302)


if __name__ == '__main__':
    app.run(debug=True)