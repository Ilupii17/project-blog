from flask import Flask, jsonify
from flask_cors import CORS
import markdown
import os
import re

app = Flask(__name__)
CORS(app)

POST_DIR = "posts"

def extract_metadata(content):
    """Extract title and description from markdown content"""
    lines = content.split('\n')
    title = None
    description = None
    
    # Extract first H1 as title
    for line in lines:
        if line.startswith('# '):
            title = line.replace('# ', '').strip()
            break
    
    # Extract first paragraph as description
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('#') and not stripped.startswith('```'):
            description = stripped[:150] + '...' if len(stripped) > 150 else stripped
            break
    
    return title, description

@app.route("/posts")
def list_posts():
    try:
        files = [f for f in os.listdir(POST_DIR) if f.endswith(".md")]
        posts = []
        
        for filename in files:
            filepath = os.path.join(POST_DIR, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    title, description = extract_metadata(content)
                    
                    posts.append({
                        "filename": filename,
                        "title": title,
                        "description": description,
                        "date": None  # You can add file modification date here
                    })
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                posts.append({
                    "filename": filename,
                    "title": None,
                    "description": None,
                    "date": None
                })
        
        return jsonify(posts)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/posts/<name>")
def get_post(name):
    filepath = os.path.join(POST_DIR, name)
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            title, description = extract_metadata(content)
            html = markdown.markdown(content, extensions=["fenced_code", "codehilite"])
            
            return jsonify({
                "filename": name,
                "title": title,
                "description": description,
                "content": html
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"error": "Post not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)