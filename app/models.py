from app import db
# Use this link for queries and examples https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
# from enum34 import Enum

# class GenderType(Enum):
#     male = "Male"
#     female = "Female"
    
# class ScreenType(Enum):
# 	desktop = "Desktop Computer"
# 	laptop = "Laptop"
# 	phonetablet = "Phone/Tablet"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    age = db.Column(db.String(64), nullable=False )
    eyesightl = db.Column(db.Float, nullable=False)
    eyesightr = db.Column(db.Float, nullable=False)
    gender = db.Column(db.String(64), nullable=False)
    screen = db.Column(db.String(64), nullable=False)
    answers = db.relationship('Answer', backref='participant', lazy='dynamic')

    def __init__(self, username, email, age,eyesightl,eyesightr,gender,screen):
       self.username = username
       self.email = email
       self.age=age
       self.eyesightl=eyesightl
       self.eyesightr=eyesightr
       self.gender=gender
       self.screen=screen

    def __repr__(self):
        return '<User %r>' % (self.username)


class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey_name = db.Column(db.String(64), nullable=False)
    questions = db.relationship('Question', backref='surveyname', lazy='dynamic')


    def __repr__(self):
        return '<Survey %r>' % (self.survey_name)


class Question(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))
	question_type = db.Column(db.String(64), nullable=False)
	question_text = db.Column(db.Text, nullable=False)

	def __repr__(self):
		return '<Question %r>' % (self.question_text)


class Answer(db.Model): 
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
	answer_text =  db.Column(db.Text, nullable=False)


	def __repr__(self):
		return '<Answer %r>' % (self.answer_text)



