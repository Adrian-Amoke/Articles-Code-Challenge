import sqlite3
from lib.db.connection import get_connection

class Author:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty string")
        self._name = value

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute(
                "INSERT INTO authors (name) VALUES (?)",
                (self.name,)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE authors SET name = ? WHERE id = ?",
                (self.name, self.id)
            )
        conn.commit()

    @classmethod
    def find_by_id(cls, author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM authors WHERE id = ?", (author_id,))
        row = cursor.fetchone()
        if row:
            return cls(id=row[0], name=row[1])
        return None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM authors WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row:
            return cls(id=row[0], name=row[1])
        return None

    def get_articles(self):
        from lib.models.article import Article
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE author_id = ?", (self.id,))
        rows = cursor.fetchall()
        return [Article(id=row[0], title=row[1], author_id=row[2], magazine_id=row[3]) for row in rows]
