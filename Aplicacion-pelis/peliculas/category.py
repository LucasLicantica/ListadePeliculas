from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from peliculas.db import get_db

bp = Blueprint('category', __name__,url_prefix="/category/")

@bp.route('/')
def index():
    db = get_db()
    peli = db.execute(
        """SELECT f.name AS titulo, l.name AS lenguaje 
         FROM film f JOIN category l ON c.category_id = f.category_id
         ORDER BY f.film_id DESC"""
    ).fetchall()
    return render_template('category/index.html', peli=peli)
