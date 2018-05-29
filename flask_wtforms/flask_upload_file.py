import os
from flask import Flask, request, render_template, send_from_directory
from forms import UploadForm
from werkzeug.datastructures import CombinedMultiDict


UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'imgs')
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('flask_upload_file.html')
    else:
        form = UploadForm(CombinedMultiDict([request.form, request.files]))
        if form.validate():
            avatar = request.files.get('avatar')
            desc = request.form.get('desc')
            avatar.save(os.path.join(UPLOAD_PATH, avatar.filename))
            print(desc)
            return '上传成功'
        else:
            print(form.errors)
            return 'fail'


@app.route('/images/<filename>')
def images(filename):
    return send_from_directory('imgs', filename)


if __name__ == '__main__':
    app.run(debug=True)