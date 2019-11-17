from flask import render_template
from flask import Flask
app = Flask(__name__)

from random import randint

my_rand = randint(0, 99)
print(f'random: {my_rand}')
top_limit = 100
bottom_limit = 0
guess = " "
tries = 0

while my_rand != guess:
  tries = tries + 1

  guess = int((top_limit + bottom_limit) / 2)

  print(f'Guess: {guess}, Toplimit: {top_limit}, Bottom limit: {bottom_limit}')

  if guess > my_rand:
    print("Guess was too high")
    top_limit = guess

  elif guess < my_rand:
    print("Guess was too low")
    bottom_limit = guess

  elif guess == my_rand:
    print(f"Correct, the number was {my_rand}!")
    final_answer = guess
    final_tries = tries


@app.route("/")
def index():
  name = 'Quintin'
  return render_template(
      'index.html',
      title='Welcome',
      username=name,
      final=final_answer,
      tries=final_tries
  )


if __name__ == "__main__":
  app.run()