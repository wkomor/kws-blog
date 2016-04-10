from flask.ext.mail import Message
from application import app
from application.decorators import async
from appengine_config import ADMINS
from flask.ext.mail import Mail

mail = Mail(app)

@async
def send_async_email(msg):
    mail.send(msg)


def send_email(subject, sender, text_body):
    msg = Message(subject, sender = sender, recipients = ADMINS)
    msg.body = text_body
    send_async_email(msg)