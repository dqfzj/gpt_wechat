from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return {
        "msg": "success",
        "data": "welcome."
    }


if __name__ == '__main__':
    app.run(port=9000)
