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

# @app.route('/bloghome')
# def bloghome():
#     return render_template("blog-home.html")

# @app.route('/blogpost')
# def blogpost():
#     return render_template("blog-post.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/faq')
def faq():
    return render_template("faq.html")

@app.route('/' subdomain="aph")
def aph():
    return render_template("aph.html")

@app.route('/ramp1000')
def RAMP1000():
    return render_template("portfolio-item-RAMP1000.html")

@app.route('/ypph')
def YPPH():
    return render_template("portfolio-item-YPPH.html")

@app.route('/way')
def TWC():
    return render_template("portfolio-item-The-WAY-Campaign.html")

@app.route('/hllp')
def HLLP():
    return render_template("portfolio-item-HLLP.html")

@app.route('/vip')
def VIP():
    return render_template("portfolio-item-VIP.html")

@app.route('/kampala')
def Kampala():
    return render_template("portfolio-item-kampala.html")

@app.route('/cso-pre-consultation-meeting-for-west-africa-region')
def CSO():
    return render_template("portfolio-item-CSO.html")

@app.route('/achieve-campaign-partnership-with-white-ribbon-alliance-nigeria')
def Achieve():
    return render_template("portfolio-item-ACHIEVE.html")

@app.route('/planetary-health-alliance')
def Planetary():
    return render_template("portfolio-item-Planetary.html")

@app.route('/legislative-network-for-universal-health-coverage-project')
def Legislative():
    return render_template("portfolio-item-Legislative.html")

@app.route('/healthcare-improvement-project')
def HCIP():
    return render_template("portfolio-item-HCIP.html")

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
    app.config['SERVER_NAME'] = "publichealth-edu.herokuapp.com'
    app.run(debug=True)
