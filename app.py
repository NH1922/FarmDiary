from flask import Flask, render_template,request
from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators, StringField, SubmitField, DecimalField
from wtforms.fields.html5 import DateField
import datetime


app = Flask(__name__)
expenses = []
budget = 0
deadline = None
village = None
current_budget = 0
remaining_budget = 0
current_expenses = 0

app.secret_key = "123456789"

class information_form(Form):
    budget = DecimalField("Budget", validators=[validators.data_required()])
    deadline = DateField("Deadline", format="%d-%m-%y",  validators=[validators.data_required()])
    hometown = StringField("Village", validators=[validators.data_required()])





@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getstarted',methods=["POST", "GET"])
def initizlize():
    return render_template("getstarted.html")


@app.route('/dashboard',methods=['POST',"GET"])
def grabvalues():
    global budget, deadline, village, current_expenses, remaining_expenses
    global expenses
    sum = 0
    global expenses
    print("before for loop")
    #print(expenses)
    for expense in expenses:
        sum = sum + int(expense['cost'])
        print(sum)
    print("After foor loop")
    current_expenses = current_expenses + sum
    remaining_expenses = int(budget) - current_expenses
    return render_template("dashboard.html", budget=budget,deadline=deadline,current_expenses=current_expenses,
                           remaining_expenses = remaining_expenses)


@app.route('/setvals',methods = ["POST","GET"])
def setvalues():
    global budget, deadline, village, current_expenses, remaining_expenses
    global expenses
    print (expenses)
    print(current_expenses)
    budget = request.form['budget']
    deadline = request.form['deadline']
    village = request.form['village']
    sum = 0
    for expense in expenses:
        print(expense['cost'])
        #sum = sum + expense['cost']
    current_expenses = current_expenses + sum
    remaining_expenses = int(budget) - current_expenses
    return render_template("dashboard.html", budget=budget, deadline=deadline, current_expenses=current_expenses,
                           remaining_expenses=remaining_expenses)



@app.route('/add',methods = ["POST","GET"])
def add_expense():
    global expenses
    entry = {}
    global budget
    print(budget)
    entry['date'] = datetime.datetime.now()
    entry['type'] = request.form.get('type')
    entry['name'] = request.form.get('name')
    entry['cost'] = request.form.get('cost')
    expenses.append(entry)
    print(expenses)
    return render_template("add.html")


@app.route("/view")
def view_expenses():
    global expenses
    return render_template("view.html", expeneses=expenses)


if __name__ == '__main__':
    app.run(debug=True)