from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True


# homepage
@app.route("/")
def index():
    return render_template("index.html")

# about page
@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

# new client intake form
@app.route("/new_client", methods=["POST", "GET"])
def new_client():
    return render_template("new_client.html")

@app.route("/new_client1", methods=["POST"])
def thanks():
    return "Thank you, " + name + "!"

app.run()