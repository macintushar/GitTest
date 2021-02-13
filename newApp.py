from flask import Flask, url_for, render_template, redirect, flash, request
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'name':'Tushar Selvakumar',
        'descr':'Created the GUI part of the project.',
        'class':'12 F',
        'roll':'4'
    },
    {
        'name':'Jainam Bafna',
        'descr':'Created the CLI part of the project.',
        'class':'12 F',
        'roll':'10'
    }
]


@app.route('/')
def home():
    return render_template('unified.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)