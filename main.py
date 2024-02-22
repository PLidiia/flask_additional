from flask import Flask

application = Flask(__name__)


@application.route("/load")
def form():
    with open('des.html', 'r', encoding='utf-8') as design_file:
        return design_file.read()


if __name__ == '__main__':
    application.run(port=8080, host='127.0.0.1', debug=True)
