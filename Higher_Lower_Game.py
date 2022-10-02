"""This script is a pretty basic use of flask to create a website for guessing numbers.  Feel free to edit and change
as you see fit.  The gifs can also be easily changed."""

# Import modules.
from flask import Flask
import random

# Create a new app object from flask.
app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)


# Create a route to the website with the heading and a gif.
@app.route("/")
def higher_lower_home():
    return '<h1 style="text-align: center">Guess a number between 0 and 9!</h1>' \
           '<img src="https://media2.giphy.com/media/l378khQxt68syiWJy/giphy.gif?cid=ecf05e47momdbzlc9ynpo3gwoi6etl74' \
           'h24bxwm6vev0b20v&rid=giphy.gif&ct=g">'


# Let user input ending for URL to guess.  The script will tell them whether they are too low, too high, or correct.
@app.route("/<int:user_guess>")
def guess(user_guess):
    if user_guess == random_number:
        return f"<h1 style='text-align: center'>Your guess of {user_guess} was totally correct!  Good job!</h1>" \
               f"<img src='https://media4.giphy.com/media/1hMk0bfsSrG32Nhd5K/giphy.gif?cid=ecf05e47r94tj2iezos6t" \
               f"0d7vgn0gyekx4b0ujjcln2jltx4&rid=giphy.gif&ct=g'>"
    elif user_guess < random_number:
        return f"<h1 style='text-align: center'>Your guess of {user_guess} was too low!  Try again!</h1>" \
               f"<img src='https://media1.giphy.com/media/azHp1od1Z3MGUjWDp0/giphy.gif?cid=ecf05e47vdww7x" \
               f"6w7wcwjkcabx20pa20gkz5e2rn4r2b754r&rid=giphy.gif&ct=g'>"
    else:
        return f"<h1 style='text-align: center'>Your guess of {user_guess} was too high!  Try again!</h1>" \
               f"<img src='https://media0.giphy.com/media/3BRDkVjKikYW4/giphy.gif?cid=ecf05e47fm9clvvde9ih" \
               f"u1mtw3f87vzt0ycr6eouthvbj028&rid=giphy.gif&ct=g'>"


if __name__ == "__main__":
    # Run the app in the debug mode to auto-reload
    app.run(debug=True)
