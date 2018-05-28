from flask_migrate_demo import create_app, config

app = create_app()
app.config.from_object(config)

@app.route('/')
def index():
    return 'hello world'


@app.route('/profile')
def profile():
    pass


if __name__ == '__main__':
    app.run()