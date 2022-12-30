from flask import Blueprint,render_template
from flask_login import login_required,current_user

views= Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("RAJAN VANIKAAR.html")

@views.route('/rec')
@login_required
def rec():
    return render_template("tryp3.html",user=current_user)

