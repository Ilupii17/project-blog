from flask import Flask, jsonify, send_from_directory
import markdown
import os

app = Flask(__name__)
POST_DIR = "posts"

@app.route("/posts")
def list_posts():
    files = [f for f in os.listdir(POST_DIR) if f.endswith(".md")]
    return jsonify(files)

@app.route("/posts/<name>")
def get_post(name):
    filepath = os.path.join(POST_DIR, name)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        html = markdown.markdown(content, extensions=["fenced_code", "codehilite"])
        return jsonify({"title": name, "content": html})
    return jsonify({"error": "Post not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)