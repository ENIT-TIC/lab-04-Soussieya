import sqlite3
import os
from flask import Flask, jsonify, request

app = Flask(__name__)
DB_PATH = os.environ.get("DB_PATH", "books.db")  # Utilise la variable d'environnement si définie

def init_db():
    """Initialise la base de données et crée la table si elle n'existe pas."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)  # Crée le dossier si inexistant
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Initialise la DB au démarrage
init_db()

# ----------- ROUTES -----------
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Books API (SQLite version)",
        "version": "2.0"
    })

@app.route('/books', methods=['GET'])
def get_books():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    rows = c.fetchall()
    conn.close()
    books = [{"id": r[0], "title": r[1], "author": r[2], "year": r[3]} for r in rows]
    return jsonify({"books": books, "count": len(books)})

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE id=?", (book_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return jsonify({"id": row[0], "title": row[1], "author": row[2], "year": row[3]})
    return jsonify({"error": "Book not found"}), 404

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO books (title, author, year) VALUES (?,?,?)",
              (data["title"], data["author"], data["year"]))
    conn.commit()
    new_id = c.lastrowid
    conn.close()
    return jsonify({"id": new_id, **data}), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    fields, values = [], []
    for col in ["title", "author", "year"]:
        if col in data:
            fields.append(f"{col}=?")
            values.append(data[col])
    values.append(book_id)
    c.execute(f"UPDATE books SET {', '.join(fields)} WHERE id=?", values)
    conn.commit()
    conn.close()
    return jsonify({"message": "Book updated"})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Book deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
