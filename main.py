from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True


# homepage
@app.route("/")
def index():
    return 

# about page
@app.route("/about", methods=["POST"])
def about():
    return 

# new client intake form
@app.route("/new_client", methods=["POST", "GET"])
def new_client():
    return 

app.run()