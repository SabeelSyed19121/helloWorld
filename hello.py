
from flask import Flask, send_file, render_template_string
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

HTML_PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Hello World Picture</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; 
           background: #fff8b3; margin: 0; padding: 2rem; }
    .card { max-width: 640px; margin: 0 auto; background: #fff; border-radius: 12px; 
            padding: 1rem; box-shadow: 0 4px 16px rgba(0,0,0,.08); }
    h1 { text-align: center; }
    img { display: block; margin: 1rem auto; border-radius: 8px; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Hello World (Image)</h1>
    /image
  </div>
</body>
</html>
"""

@app.route("/")


