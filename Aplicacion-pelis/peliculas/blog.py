from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from peliculas.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT f.title, l.name, '
        ' FROM film f JOIN language l ON l.language_id = f.language_id'
        ' ORDER BY f.film_id DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
