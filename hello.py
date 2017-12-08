from flask import Flask, render_template, send_from_directory
from flask import url_for
import hiphop

app = Flask(__name__, static_url_path='/atlassian-connect')

@app.route("/")
def status():
    return "I am alive!"

@app.route("/hit")
def action():
    hiphop.message_write()

@app.route("/atlassian-connect")
def descriptor():
    return render_template('atlassian-connect.json')
    #return url_for('static', filename='atlassian-connect.json')

if __name__ == "__main__":
    app.run(debug=True)
