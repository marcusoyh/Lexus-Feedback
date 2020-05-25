from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from send_mail import send_mail

app = Flask(__name__)

# defining database location now, env = environment
ENV = 'prod'  # now we set prod to deploy on heroku

if ENV == 'dev':
    # our personal dev database
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/lexus'
else:
    # production database, on heroku
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vikreukcaobgwl:6012a2f81ea5562933832a577933dcbd51d33acf55c7d31b5256549c751abf97@ec2-54-86-170-8.compute-1.amazonaws.com:5432/d2t6eugi9tjt5o'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text())
    startDate = db.Column(db.Date)
    endDate = db.Column(db.Date)

    def __init__(self, customer, dealer, rating, comments, startDate,endDate):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments
        self.startDate = startDate
        self.endDate = endDate


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # the 'name' that we assigned to the input text thing
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        startDate = request.form['startDate']
        endDate = request.form['endDate']

        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter required fields')

        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            # customer doesnt exist, which is what we want
            data = Feedback(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()

            # Printing all Results
            #results = Feedback.query.order_by(Feedback.startDate).all()
            print("NUMBER OF ENTRIES IN DATABASE:")
            totalCount = db.session.query(Feedback).count()
            #results = db.session.query(Feedback)
            print(totalCount)

            # Sending mail
            send_mail(customer, dealer, rating, comments,
                      startDate, endDate, totalCount)
            return render_template('success.html')
        # this is to be rendered if the user has submitted before
        return render_template('index.html', message='You have already submitted feedback')


if __name__ == '__main__':
    app.debug = True
    app.run()
