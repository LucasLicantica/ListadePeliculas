SELECT f.title AS titulo, l.name AS lenguaje 
FROM film f JOIN language l ON l.language_id = f.language_id
ORDER BY f.film_id DESC