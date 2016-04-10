from wtforms import Form, StringField, TextAreaField, \
                    HiddenField, PasswordField
from wtforms.validators import DataRequired, Email


class AddPostForm(Form):
    title = StringField(validators=[DataRequired()])
    body = TextAreaField()
    date = HiddenField()


class LoginForm(Form):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])


class ContactForm(Form):
    your_name = StringField(validators=[DataRequired()])
    your_email = StringField(validators=[DataRequired(), Email()])
    message = TextAreaField(validators=[DataRequired()])