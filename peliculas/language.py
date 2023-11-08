from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from peliculas.db import get_db

bp = Blueprint('language', __name__, url_prefix="/language/")

@bp.route('/')
def index():
    db = get_db()
    languajes = db.execute(
        """SELECT l.name AS lenguaje, l.name AS lenguaje 
         FROM film l JOIN language l ON l.language_id = f.language_id
         ORDER BY l.film_id DESC"""
    ).fetchall()
    return render_template('language/index.html', language=languajes)

