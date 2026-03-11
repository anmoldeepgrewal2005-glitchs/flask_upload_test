from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Folder to save uploaded images
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['image']  # Get uploaded file
    if image:
        filepath = os.path.join(UPLOAD_FOLDER, image.filename)
        image.save(filepath)  # Save file
        return f"Image uploaded successfully! Saved as {filepath}"
    return "No file uploaded"

if __name__ == '__main__':
    app.run(debug=True)