from werkzeug.security import generate_password_hash


class BlogModels():
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def get_username(self, username):
        db_cursor = self.db_conn.cursor(dictionary=True)
        db_cursor.execute('SELECT * FROM user WHERE username = %s', (username,))
        return db_cursor.fetchone()

    def fetch_posts(self):
        db_cursor = self.db_conn.cursor(dictionary=True)
        db_cursor.execute('SELECT p.id, title, body, created, author_id, username'
                          ' FROM post p JOIN user u ON p.author_id = u.id ORDER BY created DESC')
        return db_cursor.fetchall()

    def insert_post(self, title, body, id):
        f = open("info_logs.txt","w")
        f.write(title+body)
        db_cursor = self.db_conn.cursor()
        db_cursor.execute('INSERT INTO POST(title, body, author_id) VALUES(%s, %s, %s)', (title, body, id))
        self.db_conn.commit()

    def fetch_post(self, id):
        db_cursor = self.db_conn.cursor(dictionary=True)
        db_cursor.execute(
            'SELECT p.id, title, body, created, author_id, username FROM post p JOIN user u ON p.author_id = u.id '
            'WHERE p.id = %s', (id,))
        return db_cursor.fetchone()

    def update_post(self, title, body, id):
        db_cursor = self.db_conn.cursor()
        db_cursor.execute('UPDATE post SET title = %s, body = %s WHERE id = %s', (title, body, id))
        self.db_conn.commit()

    def delete_post(self, id):
        db_cursor = self.db_conn.cursor()
        db_cursor.execute('DELETE FROM post WHERE id = %s', (id,))
        self.db_conn.commit()

    def get_logged_user(self, user_id):
        db_cursor = self.db_conn.cursor(dictionary=True)
        db_cursor.execute(
            'SELECT * FROM user WHERE id = %s', (user_id,)
        )
        return db_cursor.fetchone()

    def get_user_id(self, username):
        db_cursor = self.db_conn.cursor(dictionary=True)
        db_cursor.execute('SELECT id FROM user WHERE username = %s', (username,))
        return db_cursor.fetchone()

    def insert_new_user(self, username, password):
        db_cursor = self.db_conn.cursor()
        db_cursor.execute(
            'INSERT INTO user (username, password) VALUES (%s, %s)',
            (username, generate_password_hash(password))
        )
        self.db_conn.commit()
