from blinker import Namespace
from datetime import datetime
from flask import request, g

namespace = Namespace()
login_signal2 = namespace.signal('login')


def login_signal(sender):
    # 用户名 ip 时间
    # username = request.args.get('username')
    ip = request.remote_addr
    now = datetime.utcnow()
    log_line = '{username}-{ip}-{now}'.format(username=g.user, ip=ip, now=now)

    with open('login_log.txt', 'a', encoding='utf-8') as f:
        f.write(log_line + '\n')

login_signal2.connect(login_signal)