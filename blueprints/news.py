from flask import Blueprint, render_template, url_for

news_bp = Blueprint('news', __name__, template_folder='news_list', static_folder='news_static')

@news_bp.route('/news')
def news():
    print(url_for('news.news_detail'))
    return render_template('news.html')


@news_bp.route('/news_list/detail')
def news_detail():
    return '这是新闻列表的详情页'
