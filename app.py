import image, os, shutil
from random import randint
from flask import Flask, Response, request, send_file, session, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["CACHE_TYPE"] = "null"

@app.route('/')
def _index():
        return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/img', methods=['POST'])
def _img():
    if 'file' not in request.files:
        return _index()
    
    file = request.files['file']
    if file.filename == '':
        return _index()

    if allowed_file(file.filename):
        img_hash = str(randint(0, 999999))
        os.remove('images/overlay.jpg')
        file.save('images/overlay.jpg')
        image.combine(img_hash)
    return render_template('image.html', i_hash = img_hash)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)