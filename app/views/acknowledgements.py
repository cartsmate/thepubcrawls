
from flask import render_template, redirect, url_for, g, session, request, flash
from app import app


@app.route('/acknowledgements')
def acknowledgements():
    print('acknowledgements')
    return render_template('acknowledgements.html', form_type='acknowledgements')
