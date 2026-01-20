
# hello.py
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
    .hint { text-align:center; color:#555; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Hello World (Image)</h1>
    /image
    <p class="hint">Served from <code>/image</code></p>
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    # Serve the HTML page that embeds the generated image
    return render_template_string(HTML_PAGE)

@app.route("/image")
def image():
    # Create an image with yellow background and centered "Hello World"
    width, height = 600, 300
    img = Image.new("RGB", (width, height), color=(255, 235, 59))  # nice yellow
    draw = ImageDraw.Draw(img)

    # Try a TrueType font; fall back to default if missing
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 48)
    except Exception:
        font = ImageFont.load_default()

    text = "Hello World"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (width - text_w) // 2
    y = (height - text_h) // 2

    # Slight shadow plus main text for contrast
    draw.text((x + 2, y + 2), text, font=font, fill=(0, 0, 0))
    draw.text((x, y), text, font=font, fill=(33, 33, 33))

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")

if __name__ == "__main__":
    # Local dev server
    app.run(host="0.0.0.0", port=5000, debug=True)

