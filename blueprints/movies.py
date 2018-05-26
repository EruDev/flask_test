from flask import Blueprint

movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/movies')
def movies():
    return '这是新闻列表'


@movies_bp.route('/movies/detail')
def movies_detail():
    return '这是新闻列表的详情页'
