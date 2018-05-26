from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'nums': -3,
        'desc': None, #'祝这世界继续热闹, 祝我仍是我'
        'info': '<script>alert("hello")</script>'
    }
    return render_template('filter.html', **context)


if __name__ == '__main__':
    app.run(debug=True)