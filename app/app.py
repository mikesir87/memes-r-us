import random
from flask import Flask, render_template
app = Flask(__name__)

# The memes we randomly choose from on each page load
MEMES = [
    "https://media.giphy.com/media/3o7qE1gDkbydaWbja0/giphy.gif",  # Hell's Kitchen: "Yes, chef."
    "https://media.giphy.com/media/XEreFwN8uA0aGjfiHK/giphy.gif",  # Great British Bake Off: Paul Hollywood
    "https://media.giphy.com/media/4vFiWupytmy03Uojqv/giphy.gif",  # NCAA March Madness: buzzer beater
]

# This function will be run whenever requests to "/" are made by the browser.
# The HTML returned from here will be sent to the browser making the request.
@app.route("/")
def index():
    message = "Welcome to Memes R Us - fresh memes, served daily!"
    meme_url = random.choice(MEMES)
    return render_template("index.html", message=message, meme_url=meme_url)

# This starts our Python app
if __name__ == "__main__":
    app.run(debug=True)