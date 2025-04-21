from flask import Flask, render_template, jsonify
from routes.api import api_bp
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Register blueprints
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def home():
    return jsonify({
        "message": "URL Shortener API",
        "endpoints": {
            "Create short URL": "POST /api/shorten",
            "Get original URL": "GET /api/shorten/<short_code>",
            "Redirect to original URL": "GET /api/redirect/<short_code>",
            "Update URL": "PUT /api/shorten/<short_code>",
            "Delete URL": "DELETE /api/shorten/<short_code>",
            "Get URL statistics": "GET /api/stats/<short_code>"
        }
    })

if __name__ == '__main__':
    app.run(debug=True)