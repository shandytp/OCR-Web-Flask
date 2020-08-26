import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from ocr_core import ocr_core

# define upload folder
UPLOAD_FOLDER = '/static/uploads/'

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

# function to check file extention
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home_page():
    return render_template('index.html')

# route to handle upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('uplaod.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):

            # save it to uploads folder
            filename = secure_filename(file.filename)
            file.save(os.path.join('static/uploads', filename))

            # call OCR function
            extracted_text = ocr_core(file)

            # extract the text and display it
            return render_template('upload.html',msg='Success', extracted_text=extracted_text, img_src= UPLOAD_FOLDER + file.filename)

    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)