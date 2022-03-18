from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

name="Jamila D. Flax"
role="Jr. Cloud Architect"
phone="914.380.0321"
email="flax.jamila@gmail.com"
location="Phoenix, AZ"


@app.route("/")
def index():
    return render_template("index.html", 
    name=name,
    role=role,
    phone=phone,
    email=email,
    location=location
    )

if __name__ == "__main__":
    app.run(debug=True)