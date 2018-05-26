from flask import Blueprint

users_bp = Blueprint('users', __name__)

@users_bp.route('/users')
def users():
    return '这是用户列表'


@users_bp.route('/users/detail')
def users_detail():
    return '这是用户列表的详情页'
