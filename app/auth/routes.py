from flask import Blueprint, render_template

auth = Blueprint("auth", __name__, template_folder="auth_templates", url_prefix="/auth")

@auth.route("/test")
def login():
    return render_template("test.html")