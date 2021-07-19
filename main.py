from flask import Flask, render_template, request, redirect, abort, url_for, flash
from flask_bootstrap import Bootstrap
import smtplib
import os

FROM_EMAIL = os.environ.get("FROM_EMAIL")
PASSWORD = os.environ.get("PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/blog-home')
def bloghome():
    return render_template("blog-home.html")

@app.route('/blog-post')
def blogpost():
    return render_template("blog-post.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/faq')
def faq():
    return render_template("faq.html")

@app.route('/Academy-of-Public-Health')
def aph():
    return render_template("aph.html")

@app.route('/portfolio-item')
def portfolioitem():
    return render_template("portfolio-item.html")

@app.route('/portfolio-overview')
def portfoliooverview():
    return render_template("portfolio-overview.html")



# @app.route('/form_entry', methods=['POST'])
# def receive_data():
#     name = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone']
#     message = request.form['message']

#     print(name)
#     print(email)
#     print(phone)
#     print(message)

#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=FROM_EMAIL, password=PASSWORD)
#         connection.sendmail(
#             from_addr=FROM_EMAIL,
#             to_addrs=TO_EMAIL,
#             msg=f"Subject: Client from Website\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
#                     )
    
#     return render_template('success.html')


if __name__ == "__main__":
    app.run(debug=True)
