from shopping_website import app
from flask import render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['UPLOAD_EXTENSIONS']


@app.route('/')
def add_products():
    return render_template('products/add_products.html')

@app.route('/success', methods=['GET', 'POST'])
def success():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        flash(file.filename)
        flash(app.config['UPLOAD_FOLDER'])
        flash(allowed_file(file.filename))
        flash(file.filename.rsplit('.', 1)[1].lower())
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('success'))

    return render_template('products/success.html')
