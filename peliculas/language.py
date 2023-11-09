from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from peliculas.db import get_db

bp = Blueprint('language', __name__, url_prefix="/language/")

@bp.route('/')
def index():
    db = get_db()
    languages = db.execute(
        """SELECT l.name, l.language_id FROM language l 
         ORDER BY l.language_id DESC"""
    ).fetchall()
    return render_template('language/index.html', languages=languages)

