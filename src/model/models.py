from flask import g
from src.model.db import get_db


def get_username(username):
    db = get_db()
    return db.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
    ).fetchone()


def fetch_posts():
    db = get_db()
    return db.execute('SELECT p.id, title, body, created, author_id, username'
                      ' FROM post p JOIN user u ON p.author_id = u.id ORDER BY created DESC').fetchall()


def insert_post(title, body):
    db = get_db()
    db.execute('INSERT INTO POST(title, body, author_id) VALUES(?, ?, ?)', (title, body, g.user['id']))
    db.commit()


def fetch_post(id):
    get_db().execute(
        'SELECT p.id, title, body, created, author_id, username FROM post p JOIN user u ON p.author_id = u.id '
        'WHERE p.id = ?',
        (id,)).fetchone()


def update_post(title, body, id):
    db = get_db()
    db.execute('UPDATE post SET title = ?, body = ? WHERE id = ?', (title, body, id))
    db.commit()


def delete_post(id):
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
