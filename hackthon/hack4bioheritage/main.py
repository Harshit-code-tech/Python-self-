def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_form():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']

        # If no file is selected, browser also submits an empty part
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Image uploaded successfully!')
            # (Optional) You can't display the image here, but you could store the filename for later retrieval
            return redirect(url_for('upload_form'))

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
