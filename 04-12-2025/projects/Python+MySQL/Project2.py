
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    passwd="V@ishnav1",
    db="retail_app2",
    autocommit=True
)
cur = conn.cursor()

# --- Minimal schema (run once) ---
cur.execute("""
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50)
)""")
cur.execute("""
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50)
)""")
cur.execute("""
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE
)""")
cur.execute("""
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10,2)
)""")

# --- Seed a few rows (safe inserts) ---
cur.execute("INSERT INTO customers VALUES (1,'Aisha'),(2,'Rahul')")
cur.execute("INSERT INTO products VALUES (101,'Laptop','Electronics'),(102,'Mouse','Electronics')")
cur.execute("INSERT INTO orders VALUES (1001,1,'2025-01-10'),(1002,2,'2025-01-12')")
cur.execute("INSERT INTO order_items VALUES (1,1001,101,1,50000.00),(2,1001,102,2,500.00),(3,1002,102,1,600.00)")

# --- Simple analytics: Top customers by revenue ---
cur.execute("""
SELECT o.customer_id, c.name, SUM(oi.quantity * oi.price) AS revenue
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
JOIN customers c ON c.customer_id = o.customer_id
GROUP BY o.customer_id, c.name
ORDER BY revenue DESC
LIMIT 5
""")
for row in cur.fetchall():
    print(row)  # (customer_id, name, revenue)

# --- Product-wise revenue ---
cur.execute("""
SELECT p.product_name, SUM(oi.quantity * oi.price) AS revenue
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
""")
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()
