from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from peliculas.db import get_db

bp = Blueprint('language', __name__, url_prefix="/language/")

@bp.route('/')
def index():
    db = get_db()
    peli = db.execute(
        """SELECT f.title AS titulo, l.name AS lenguaje 
         FROM film f JOIN language l ON l.language_id = f.language_id
         ORDER BY f.film_id DESC"""
    ).fetchall()
    return render_template('language/index.html', peli=peli)
