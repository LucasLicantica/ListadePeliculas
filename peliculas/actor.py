from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from peliculas.db import get_db

bp = Blueprint('actor', __name__, url_prefix="/actor/")
bpapi = Blueprint('api_category', __name__, url_prefix='/api/category/')

@bp.route('/')
def index():
    db = get_db()
    actores = db.execute(
        """SELECT first_name, last_name   
         FROM actor ORDER BY first_name, last_name"""
    ).fetchall()
    return render_template('actor/index.html', actores=actores)

@bp.route('/detalle/<int:id>')
def detalle(id):
    db = get_db()
    actores = db.execute(
        """SELECT first_name as nombre, last_name as apellido   
         FROM actor ORDER BY first_name, last_name
         WHERE actor_id = ?""", 
         (id,)
    ).fetchone()

    peliculas = db.execute(
        """SELECT f.title AS titulo, l.name AS lenguaje, f.release_year, f.description
         FROM film f JOIN language l ON l.language_id = f.language_id
         WHERE f.film_id = ?""", 
         (id,)
    ).fetchone()

    return render_template('peliculas/detalle.html', peliculas=peliculas, actores=actores)

#----------------------------------json---------------------------------------------------

@bpapi.route('/')
def index_api():
    db = get_db()
    actores = db.execute(
        """SELECT l.name, l.language_id FROM language l 
         ORDER BY l.language_id DESC"""
    ).fetchall()
    return jsonify(actores=actores)
