from flask import Flask, render_template

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD_': True
})

@app.route('/')
def index():
    context = {
        'username': ['zhangsan', 'lisi', 'wangwu'],
        'person':{
            'name': 'stone',
            'age': 18,
            'addr': '北京',
        },
        'book_list': [
            {
                'name': '三国演义',
                'author': '罗贯中',
                'price': 110,
            },
            {
                'name': '西游记',
                'author': '吴承恩',
                'price': 113,
            },
            {
                'name': '红楼梦',
                'author': '曹雪芹',
                'price': 120,
            },
            {
                'name': '水浒传',
                'author': '施耐庵',
                'price': 100,
            },
        ]

    }
    return render_template('flask_for.html', **context)

if __name__ == '__main__':
    app.run()