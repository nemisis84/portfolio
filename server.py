from flask import Flask, render_template, request, redirect
import sys
import csv
import send_email

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("./index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route("/submit_form", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        email = data['email']
        subject = data['subject']
        message = data['message']
        # Confirm to the user that the message is recieved
        send_email.send_an_email(
            "sender", f"No-reply; subject: {subject}", "Thank you for reaching out, I will answer your message ASAP.", email)
        # Notify me
        send_email.send_an_email(
            "sender", f"No-reply; subject: {subject}", message, "your.email@domain.com")
        return redirect("/thanks.html")
    else:
        return "something wrong"


def write_to_csv(data):
    try:
        f = open("database.csv", "a", newline='')
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer = csv.writer(
            f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email, subject, message])
        return 1
    except IOError as err:
        print(err)
        return 0


def write_to_file(data):
    try:
        f = open("Web_server/database.txt", "a")
        email = data['email']
        subject = data['subject']
        message = data['message']
        f.write(f"\n{email}, {subject}, {message}")
        return 1
    except IOError as err:
        print(err)
        return 0

# @app.route('/<username>/<int:post_id>')
# def username(username=None, post_id=None):
#     return render_template("./index.html", name=username, post_id=post_id)

# @app.route("/<unknown>")
# def unknown_url(unknown):
#     return "Ops, this site doesn't exsist"
