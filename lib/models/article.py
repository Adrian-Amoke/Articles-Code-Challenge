import sqlite3
from lib.db.connection import get_connection

class Article:
    def __init__(self, id=None, title=None, author_id=None, magazine_id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Title must be a non-empty string")
        self._title = value

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute(
                "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                (self.title, self.author_id, self.magazine_id)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE articles SET title = ?, author_id = ?, magazine_id = ? WHERE id = ?",
                (self.title, self.author_id, self.magazine_id, self.id)
            )
        conn.commit()

    @classmethod
    def find_by_id(cls, article_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE id = ?", (article_id,))
        row = cursor.fetchone()
        if row:
            return cls(id=row[0], title=row[1], author_id=row[2], magazine_id=row[3])
        return None

    @classmethod
    def find_by_title(cls, title):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE title = ?", (title,))
        row = cursor.fetchone()
        if row:
            return cls(id=row[0], title=row[1], author_id=row[2], magazine_id=row[3])
        return None

    @classmethod
    def find_by_author(cls, author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE author_id = ?", (author_id,))
        rows = cursor.fetchall()
        return [cls(id=row[0], title=row[1], author_id=row[2], magazine_id=row[3]) for row in rows]

    @classmethod
    def find_by_magazine(cls, magazine_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE magazine_id = ?", (magazine_id,))
        rows = cursor.fetchall()
        return [cls(id=row[0], title=row[1], author_id=row[2], magazine_id=row[3]) for row in rows]
