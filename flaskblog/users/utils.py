import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, fext = os.path.splitext(form_picture.filename)
    picture_name = random_hex + fext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_name)
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_name

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset request', sender='nikkolasnv1997@gmail.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simpy ignore this email.
'''
    mail.send(msg)