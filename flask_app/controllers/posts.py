from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post

from flask import render_template, redirect, session, request

@app.route('/add/post')
def addPost():
    return render_template('addPost.html')

@app.route('/create/post', methods = ['POST'])
def createPost():
    # Duhet shtuar validimet e formes
    data = {
        'title': request.form['title'],
        'content': request.form['content'],
        'user_id': session['user_id']
    }
    Post.save(data)
    return redirect('/')

@app.route('/delete/post/<int:id>')
def deletePost(id):
    data = {
        'post_id': id
    }
    post = Post.get_post_by_id(data)
    if session['user_id'] == post['user_id']:
        Post.delete(data)
        return redirect('/')
    return redirect('/')

@app.route('/post/<int:id>')
def showPost(id):
    data = {
        'post_id': id
    }
    myPost = Post.get_post_by_id(data)
    return render_template('showPost.html', post = myPost)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/loginPage')