from flask import render_template, flash, redirect
from app import app, db
from .forms import ParticipantForm
from .models import User, Survey, Question, Answer

curent_user = 0 #User number who has logged in
logged_in = 0 #Set when someone is logged in 

# Image files to be shown for questions in survey_one, survey_two, survey _three
files_for_one = []
files_for_two = []
files_for_three = [] 


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = ParticipantForm()
    if form.validate_on_submit():
        #Store Participant details in DB
        p = User(form.username.data, form.email.data, form.age.data, form.eyesightl.data, form.eyesightr.data, form.gender.data, form.screen.data)
        db.session.add(p)
        db.session.commit()
        pid = p.id
        #Start session with participant id from DB
        session["ParticipantID"] = pid
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)


# @app.route('/index')
# def index():
#     """
#     Show all the 3 experiments. Status if submitted or not If 
#     """
#     return render_template('index.html')
#What will the session 

@app.route('/survey_two')
def survey_two():
    question_number
    list_of_colors = ['#00feae','#9cff00','#ff8c00', '#e3ff00', '#857655','#ed1c24','#51422b', 
                      '#7d6d4b', '#655533', '#7a7989', '#717a99','#8f9fc3', '#9aa2b5', '#8598c0',
                       '#a1aed1', '#5f6d6e', '#887362', '#ff00ff','#8800ff','#2600ff']
    centre_color =  '#f2f1f7'
    return render_template('question2.html',list_of_colors=list_of_colors,centre_color=centre_color)

@app.route('/survey_one', methods=['GET', 'POST'])
def survey_one():
	return render_template('question.html')

@app.route('/survey_three', methods=['GET', 'POST'])
def survey_three():
    return render_template('question3.html')