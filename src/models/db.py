import click
import mysql.connector
from flask.cli import with_appcontext


def get_db():
    db_conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='blog')
    return db_conn


def init_db():
    db = get_db()
    conn = db.cursor()
    for line in open('src/model/schema.sql'):
        if line.strip():
            conn.execute(line)
    conn.close()
    return db


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.cli.add_command(init_db_command)
