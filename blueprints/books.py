from flask import Blueprint, render_template

books_bp = Blueprint('books', __name__, url_prefix='/books', template_folder='book_list', static_folder='book_static')

@books_bp.route('/list')
def books():
    return render_template('books.html')


@books_bp.route('/book_list/detail')
def books_detail():
    return '这是图书列表的详情页'
