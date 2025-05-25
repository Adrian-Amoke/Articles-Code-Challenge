import sqlite3
from lib.db.connection import get_connection

class Magazine:
    def __init__(self, id=None, name=None, category=None):
        self.id = id
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute(
                "INSERT INTO magazines (name, category) VALUES (?, ?)",
                (self.name, self.category)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE magazines SET name = ?, category = ? WHERE id = ?",
                (self.name, self.category, self.id)
            )
        conn.commit()

    @classmethod
    def find_by_id(cls, magazine_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category FROM magazines WHERE id = ?", (magazine_id,))
        row = cursor.fetchone()
        if row:
            return cls(id=row[0], name=row[1], category=row[2])
        return None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category FROM magazines WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row:
            return cls(id=row[0], name=row[1], category=row[2])
        return None

    @classmethod
    def find_by_category(cls, category):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category FROM magazines WHERE category = ?", (category,))
        rows = cursor.fetchall()
        return [cls(id=row[0], name=row[1], category=row[2]) for row in rows]

    def get_articles(self):
        from lib.models.article import Article
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE magazine_id = ?", (self.id,))
        rows = cursor.fetchall()
        return [Article(id=row[0], title=row[1], author_id=row[2], magazine_id=row[3]) for row in rows]
