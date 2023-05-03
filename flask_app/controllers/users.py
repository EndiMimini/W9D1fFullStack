from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, session, request

@app.route('/')
def index():
    #I will retreave all the users in my database
    users = User.get_all()
    return render_template('users.html', users= users)


@app.route('/add/user')
def addUser():
    return render_template('addUser.html')

@app.route('/create/user', methods = ['POST'])
def createUser():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/')

@app.route('/update/<int:id>')
def updateUser(id):
    data = {
        'user_id': id
    }
    userClicked = User.get_user_by_id(data)
    return render_template('edit.html', user = userClicked)


@app.route('/update/<int:id>', methods= ['POST'])
def updateUserInDb(id):
    data = {
        'user_id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    User.update(data)
    return redirect('/')

@app.route('/delete/<int:id>')
def deleteUser(id):
    data = {
        'user_id': id,
    }
    User.delete(data)
    return redirect(request.referrer)
