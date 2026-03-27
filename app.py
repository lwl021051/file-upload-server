from flask import Flask, request, send_from_directory, render_template_string
import os
import sys

app = Flask(__name__)

# Determine the base folder depending on whether running as PyInstaller executable
if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>File Share</title>
</head>
<body>
  <h1>Upload File</h1>
  <form action="/upload" method="post" enctype="multipart/form-data">
    <input type="file" name="file">
    <button type="submit">Upload</button>
  </form>

  <h2>Available Files</h2>
  <ul>
    {% for file in files %}
      <li><a href="/download/{{ file }}">{{ file }}</a></li>
    {% endfor %}
  </ul>

  <p><a href="/shutdown">❌ Stop Server</a></p>
</body>
</html>
"""

@app.route("/")
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template_string(HTML_PAGE, files=files)

@app.route("/upload", methods=["POST"])
def upload():
    f = request.files["file"]
    f.save(os.path.join(UPLOAD_FOLDER, f.filename))
    return "✅ Upload successful! <a href='/'>Go back</a>"

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route("/shutdown")
def shutdown():
    shutdown_server = request.environ.get("werkzeug.server.shutdown")
    if shutdown_server is None:
        return "❌ Not running with the Werkzeug Server"
    shutdown_server()
    return "🛑 Server shutting down..."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8069)
