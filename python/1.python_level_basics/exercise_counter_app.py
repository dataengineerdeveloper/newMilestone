from flask import Flask, render_template_string
from random import choice



app = Flask(__name__)

computer_number = choice(range(1,101))
print(f'computer pickerd{computer_number}')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        guess = int(request.form['number_guess'])
        message = check_number_show_message(guess,computer_number)
        guesses.append(guess)
        print(guesses)
        print(message) 
    return render_template('index.html', guesses=guesses)

@app.route('/reset')
def reset():
    return 'Reset page'
          