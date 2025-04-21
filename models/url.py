from datetime import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from utils.shortcode import generate_short_code

# Load environment variables
load_dotenv()

# MongoDB connection
client = MongoClient(os.getenv('MONGO_URI'))
db = client[os.getenv('DB_NAME')]
urls_collection = db['urls']

class URLModel:
    @staticmethod
    def create_url(original_url):
        """Create a new short URL entry in the database"""
        # Generate a unique short code
        while True:
            short_code = generate_short_code()
            if not urls_collection.find_one({'shortCode': short_code}):
                break
        
        # Create a new document
        now = datetime.utcnow().isoformat() + 'Z'
        url_doc = {
            'url': original_url,
            'shortCode': short_code,
            'createdAt': now,
            'updatedAt': now,
            'accessCount': 0
        }
        
        # Insert into database
        result = urls_collection.insert_one(url_doc)
        
        # Add the ID to the document
        url_doc['id'] = str(result.inserted_id)
        
        return url_doc
    
    @staticmethod
    def get_url_by_code(short_code):
        """Retrieve a URL by its short code"""
        url_doc = urls_collection.find_one({'shortCode': short_code})
        if url_doc:
            url_doc['id'] = str(url_doc.pop('_id'))
            return url_doc
        return None
    
    @staticmethod
    def update_url(short_code, new_url):
        """Update an existing URL"""
        now = datetime.utcnow().isoformat() + 'Z'
        result = urls_collection.update_one(
            {'shortCode': short_code},
            {'$set': {
                'url': new_url,
                'updatedAt': now
            }}
        )
        
        if result.modified_count:
            url_doc = urls_collection.find_one({'shortCode': short_code})
            url_doc['id'] = str(url_doc.pop('_id'))
            return url_doc
        return None
    
    @staticmethod
    def delete_url(short_code):
        """Delete a URL by its short code"""
        result = urls_collection.delete_one({'shortCode': short_code})
        return result.deleted_count > 0
    
    @staticmethod
    def increment_access_count(short_code):
        """Increment the access count for a URL"""
        result = urls_collection.update_one(
            {'shortCode': short_code},
            {'$inc': {'accessCount': 1}}
        )
        return result.modified_count > 0
