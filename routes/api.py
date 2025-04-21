from flask import Blueprint, request, jsonify, redirect
from models.url import URLModel
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
BASE_URL = os.getenv('BASE_URL')

# Create Blueprint
api_bp = Blueprint('api', __name__)

@api_bp.route('/shorten', methods=['POST'])
def create_short_url():
    """Create a new short URL"""
    data = request.get_json()
    
    # Validate input
    if not data or 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400
    
    original_url = data['url']
    
    # Basic URL validation
    if not original_url.startswith(('http://', 'https://')):
        return jsonify({'error': 'Invalid URL format. URL must start with http:// or https://'}), 400
    
    # Create short URL
    url_doc = URLModel.create_url(original_url)
    
    return jsonify(url_doc), 201
@api_bp.route('/shorten/<short_code>', methods=['GET'])
def get_original_url(short_code):
    """Retrieve the original URL from a short code"""
    url_doc = URLModel.get_url_by_code(short_code)
    
    if not url_doc:
        return jsonify({'error': 'Short URL not found'}), 404
    
    return jsonify(url_doc), 200