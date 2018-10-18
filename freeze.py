from pathlib import Path
from flask_frozen import Freezer
from flask_app import app

freezer = Freezer(app)

@freezer.register_generator
def blog():
    p = Path('pages')
    pages = [x.stem for x in p.iterdir()]
    for page in pages:
        yield {'path': page}

if __name__ == '__main__':
    freezer.freeze()
