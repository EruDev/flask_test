from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with
import config
from exts import db
from models import User, Article, Tag

app = Flask(__name__)
app.config.from_object(config)
api = Api(app)
db.init_app(app)


class Article_view(Resource):

    resource_fields = {
        'article_title': fields.String(attribute='title'),
        'content': fields.String,
        'author': fields.Nested({
           'username':fields.String,
            'email': fields.String,
        }),
        'tags': fields.List(fields.Nested({
            'id': fields.Integer,
            'name': fields.String,
        })),
        'read_count': fields.Integer(default=100),
    }

    @marshal_with(resource_fields)
    def get(self, article_id):
        article = Article.query.get(article_id)
        return article

api.add_resource(Article_view, '/article/<article_id>', endpoint='article')


# class Article(object):
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#
# article = Article('aaa', 'xxx')
#
#
# class Post(Resource):
#     resource_fields = {
#         'title': fields.String,
#         'content': fields.String,
#     }
#     @marshal_with(resource_fields)
#     def get(self):
#         return article

# api.add_resource(Post, '/post', endpoint='post')

@app.route('/')
def index():
    user = User(username='zhangsan', email='zhangsan@qq.com')
    article = Article(title='flask is cool')
    article.author = user
    tag1 = Tag(name='Python')
    tag2 = Tag(name='Scrapy')
    article.tags.append(tag1)
    article.tags.append(tag2)
    db.session.add(article)
    db.session.commit()
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)