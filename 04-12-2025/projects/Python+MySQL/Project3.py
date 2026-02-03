
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    passwd="V@ishnav1",
    db="library_db",   # create/use this DB
    autocommit=True
)
cur = conn.cursor()

# --- Tables (run once) ---
cur.execute("""
CREATE TABLE IF NOT EXISTS books(
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    available TINYINT DEFAULT 1
)
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS members(
    member_id INT PRIMARY KEY,
    member_name VARCHAR(100)
)
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS borrows (
    borrow_id INT PRIMARY KEY,
    member_id INT,
    book_id INT,
    borrow_date DATE,
    return_date DATE NULL
)
""")

# --- Seed data ---
cur.execute("INSERT IGNORE INTO books VALUES (1,'Python Basics','John Doe',1),(2,'Data Science 101','Alice',1)")
cur.execute("INSERT IGNORE INTO members VALUES (101,'Meera Iyer'),(102,'Rahul Sharma')")

# --- Search by title/author ---
keyword = "Python"
cur.execute("SELECT book_id, title, author, available FROM books WHERE title LIKE %s OR author LIKE %s",
            (f"%{keyword}%", f"%{keyword}%"))
for r in cur.fetchall():
    print(r)

# --- Borrow a book (mark unavailable) ---
cur.execute("UPDATE books SET available=0 WHERE book_id=1")

# --- Return book (mark available) ---
cur.execute("UPDATE books SET available=1 WHERE book_id=1")

cur.close()
conn.close()
