from wtforms import Form, StringField, TextAreaField, HiddenField, PasswordField
from wtforms.validators import DataRequired


class AddPostForm(Form):
    title = StringField(validators=[DataRequired()])
    body = TextAreaField()
    date = HiddenField()


class LoginForm(Form):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])