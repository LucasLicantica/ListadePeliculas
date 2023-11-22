from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from peliculas.db import get_db

bp = Blueprint('category', __name__,url_prefix="/category/")
bpapi = Blueprint('api_category', __name__, url_prefix='/api/category/')

@bp.route('/')
def index():
    db = get_db()
    categories = db.execute(
        """SELECT c.name AS category, c.name AS categoria 
         FROM film c JOIN category c ON l.category_id = f.category_id
         ORDER BY c.film_id DESC"""
    ).fetchall()
    return render_template('category/index.html', category=categories)

@bp.route('/detalle/<int:id>')
def detalle(id):
    db = get_db()
    categories = db.execute(
        """SELECT c.name AS category, c.name AS categoria 
         FROM film c JOIN category c ON l.category_id = f.category_id
         ORDER BY c.film_id DESC""", 
         (id,)
    ).fetchone()
    return render_template('categories/detalle.html', category=categories)

@bpapi.route('/')
def index_api():
    db = get_db()
    categories = db.execute(
        """SELECT c.name AS category, c.name AS categoria 
         FROM film c JOIN category c ON l.category_id = f.category_id
         ORDER BY c.film_id DESC"""
    ).fetchall()
    return jsonify(category=categories)
