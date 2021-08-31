from flask import Flask, render_template, url_for, redirect, session, request, g
app = Flask(__name__)
app.static_folder = 'static'




@app.route("/login", methods=['GET', 'POST'])
def login_main():
    return render_template('login.html')
        
@app.route("/")
@app.route("/home")
def home_main():
    return render_template('home.html', title="Home")

@app.route("/webscrape")
def survey_main():
    return render_template('webscrape.html')

@app.route("/configgen")
def prep_main():
    return render_template('configgen.html')

@app.route("/deployment")
def deployment_main():
    return render_template('deployment.html')

@app.route("/validation")
def validation_main():
    return render_template('validation.html')

@app.route("/integrationengineer")
def integrationengineer_main():
    return render_template('integrationengineer.html')

if __name__ == "__main__":
    app.run(debug=True, host='192.168.0.135')

