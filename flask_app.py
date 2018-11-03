from flask import Flask, render_template, Markup
from flask_scss import Scss
from markdown import markdown

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def index():
    return render_template('index.html')

"""
@app.route("/blog/<path>.html")
def blog(path):
    with open('pages/' + path + '.md') as f:
        content = f.read().split('\n\n', 1)
        metadata = content[0]
        post_content = Markup(markdown(content[1]))
    return render_template('blog.html', content=post_content)
"""

if __name__ == '__main__':
    Scss(app, static_dir='static', asset_dir='assets')
    app.run(port=8000, debug=True)
