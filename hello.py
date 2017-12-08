from flask import Flask, json, render_template
import hiphop

app = Flask(__name__)

@app.route("/")
def status():
    return "I am alive!"

@app.route("/hit")
def action():
    hiphop.message_write()

@app.route("/atlassian-connect.json")
    def descriptor():
        data = json.load(open(atlassian-connect.json))
        return data

if __name__ == "__main__":
    app.run()
