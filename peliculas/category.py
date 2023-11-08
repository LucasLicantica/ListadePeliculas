from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from peliculas.db import get_db

bp = Blueprint('category', __name__,url_prefix="/category/")

@bp.route('/')
def index():
    db = get_db()
    categorias = db.execute(
        """SELECT c.name AS category, c.name AS categoria 
         FROM film c JOIN category c ON l.category_id = f.category_id
         ORDER BY c.film_id DESC"""
    ).fetchall()
    return render_template('category/index.html', category=categorias)
