from flask import Flask, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configure upload folder (replace with your desired path)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Allowed extensions for uploaded files
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
