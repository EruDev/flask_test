from flask import Flask
from blueprints.books import books_bp
from blueprints.movies import movies_bp
from blueprints.news import news_bp
from blueprints.users import users_bp

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True
})
app.register_blueprint(books_bp)
app.register_blueprint(movies_bp)
app.register_blueprint(news_bp)
app.register_blueprint(users_bp)

@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()