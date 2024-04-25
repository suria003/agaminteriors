from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
db = SQLAlchemy(app)

class Contact(db.Model):
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    
class Estimate(db.Model):
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    
class Payment(db.Model):
    name = db.Column(db.String(100), nullable=False)
    product = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return '<Client %r>' % self.name

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/contactData", methods = ['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['userName']
        number = request.form['userNumber']
        email = request.form['userEmail']
        
        new_client1 = Contact(name=name, number=int(number), email=email)
        db.session.add(new_client1)
        db.session.commit()
        
        return redirect(url_for('index'))
    
@app.route("/api/estimateData", methods =['POST'])
def estimate():
    if request.method == 'POST':
        name = request.form['userEstimateName']
        number = request.form['userEstimateNumber']
        location = request.form['userEstimateLocation']
        
        new_client2 = Estimate(name=name,  number=int(number), location=location)
        db.session.add(new_client2)
        db.session.commit()
        
        return redirect(url_for('index'))
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/404Page')
def errorPage():
    return render_template('404.html')

@app.route('/kitchen/payment', methods = ['POST'])
def payment():
    if request.method == 'POST':
        name = request.form['username']
        product = request.form['kitchenProductDataset']
        number = request.form['kitchenProductContact']
        email = request.form['kitchenProductEmail']
        location = request.form['kitchenProductLocation']
        
        new_dataset = Payment(name=name, product=product, number=number, email=email, location=location)
        db.session.add(new_dataset)
        db.session.commit()
        
        return render_template('orderComplete.html')
    
@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/contactDataSet')
def view_contacts():
    contacts = Contact.query.all()
    return render_template('adminContacts.html', contacts=contacts)

@app.route('/paymentDataSet')
def view_payments():
    payments = Payment.query.all()
    return render_template('adminPayment.html', payments=payments)

@app.route('/freeEstimate')
def view_estimate():
    estimates = Estimate.query.all()
    return render_template('adminEstimate.html', estimates=estimates)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False, host='0.0.0.0')
