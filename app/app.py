import random
from flask import Flask, render_template
app = Flask(__name__)

MEMES = [
    {
        "url": "https://media.giphy.com/media/l0HlOBZer3pIVRmU8/giphy.gif",
        "title": "The Winning Goal — Extended Celebration Edition",
        "reviews": "3,847,201",
    },
    {
        "url": "https://media.giphy.com/media/14hs7g86sQqDF6/giphy.gif",
        "title": "Penalty Shootout Stress Reaction Bundle",
        "reviews": "1,204,993",
    },
    {
        "url": "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
        "title": "Referee Decision Disbelief — Classic Collection",
        "reviews": "2,019,482",
    },
]

# This function will be run whenever requests to "/" are made by the browser.
# The HTML returned from here will be sent to the browser making the request.
@app.route("/")
def index():
    meme = random.choice(MEMES)
    return render_template("index.html", meme=meme)

# This starts our Python app
if __name__ == "__main__":
    app.run(debug=True)