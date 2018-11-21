from pathlib import Path
from datetime import datetime
from blog_engine import add_metadata
from flask import Flask, render_template, Markup
from flask_scss import Scss
from blog_engine.parse_markdown import render_post
import json
import config

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/blog/<name>.html")
def posts(name):
    filename = f'content/{name}.md'

    with open(filename) as f:
        metadata = render_post(f.read())
        post_content = Markup(metadata['content'])
        title = metadata['title']
        created_time = metadata.get('date', datetime.fromtimestamp(Path(filename).stat().st_ctime).strftime("%Y-%m-%d"))
        author = metadata.get('author', config.AUTHOR)
    return render_template('blog.html', 
            content = post_content,
            title = title,
            author = author,
            created = created_time)


@app.route("/posts.html")
def blog():
    with open('title_list.json') as j:
        title_list = json.loads(j.read())
    return render_template('blog_list.html', title_list=title_list)


if __name__ == '__main__':
    Scss(app, static_dir='static', asset_dir='assets')
    app.run(host='0.0.0.0', port=8000, debug=True)
