import hashlib
from application import app
# from google import appengine
from flask import render_template, request, url_for, redirect, \
                    session, abort, flash
from application.models import BlogPost, User
from application.forms import AddPostForm, LoginForm
from datetime import datetime
from flask.ext.login import LoginManager, login_required, login_user, logout_user
from wtforms import Form
from wtforms.ext.appengine.db import model_form
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def index():
    """
    Main page with posts list
    """
    return render_template('index.html')


@app.route('/posts')
def posts():
    """
    Function to load posts
    """
    page = 0
    if request.args.get('page'):
        page = int(request.args.get('page'))
    posts = BlogPost.all().order('-date').order('title').run(limit=2, offset=page)
    return render_template('posts.html', posts=posts)


@app.route('/post/<id>')
def post_detail(id):
    """
    detail view for post
    Args:
        id (int): id of post
    """
    post = BlogPost.get_by_id(int(id))
    return render_template('detail.html', post=post)


@app.route('/add_post', methods=['GET', 'POST'])
@login_required
def add_post():
    """
    Form to add post
    """
    form = AddPostForm(request.form)
    if request.method == 'POST':
        post = BlogPost()
        post.title = form.title.data
        post.body = form.body.data
        post.date = datetime.strptime(form.date.data, "%d.%m.%Y")
        post.put()
        return redirect(url_for('admin_view'))
    return render_template('add_post.html', form=form)


@app.route('/admin')
@login_required
def admin_view():
    posts = BlogPost.all()
    return render_template('admin.html', posts=posts)


@app.route("/edit/<id>", methods = ['GET', 'POST'])
def edit(id):
    MyForm = model_form(BlogPost, Form)
    post = BlogPost.get_by_id(int(id))
    form = MyForm(request.form, post)

    if request.method == "POST":
        form.populate_obj(post)
        post.put()
        print post
        flash("Post updated")
        return redirect(url_for("admin_view"))
    return render_template("edit.html", form=form)


@login_manager.user_loader
def load_user(id):
    return User()


@app.route('/login', methods = ['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        # Login and validate the user.
        # user should be an instance of your `User` class
        user = load_user(form.username.data)
        if (user is not None):
            m = hashlib.md5()
            m.update('form.password.data')
            print m.hexdigest()
            if user.id == form.username.data and \
                            user.password == m.hexdigest():
                login_user(user)
                flash('Logged in successfully.')
                return redirect(url_for('index'))
            else:
                flash('Login or password are incorrect')
    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/delete/post/<id>")
@login_required
def delete(id):
    post = BlogPost.get_by_id(int(id))
    if post:
        print(post)
        post.delete()
        redirect(url_for('admin_view'))
    return redirect(url_for('admin_view'))

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contacts")
def contacts():
    return render_template('contacts.html')

@app.before_request
def csrf_protect():
    """
    Provide csrf token
    """
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = 'fdgfgsegrae434fvsdgre5gsgfbrtbhtrb5432g'
    return session['_csrf_token']


app.jinja_env.globals['csrf_token'] = generate_csrf_token


