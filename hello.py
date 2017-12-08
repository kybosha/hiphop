from flask import Flask
import hiphop

app = Flask(__name__)

@app.route("/")
def action():
    return "I am alive!"

@app.route("/hit"):
    hiphop.message_write()

if __name__ == "__main__":
    app.run()
