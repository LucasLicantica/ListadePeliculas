from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from peliculas.db import get_db

bp = Blueprint('actor', __name__, url_prefix="/actor/")

@bp.route('/')
def index():
    db = get_db()
    peli = db.execute(
        """SELECT f.title AS titulo, l.name AS actor 
         FROM film f JOIN actor l ON l.language_id = f.actor_id
         ORDER BY f.film_id DESC"""
    ).fetchall()
    return render_template('actor/index.html', peli=peli)
