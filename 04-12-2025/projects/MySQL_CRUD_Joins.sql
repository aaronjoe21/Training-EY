-- 40. Create a database retail_app and two tables: customers and orders. Insert 10 rows.

CREATE DATABASE retail_app;
USE retail_app;

CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  name VARCHAR(50)
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  amount DECIMAL(10,2),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Insert customers
INSERT INTO customers VALUES
(1,'Aisha'),(2,'Rahul'),(3,'Meera'),(4,'Sanjay'),(5,'Priya'),
(6,'Imran'),(7,'Neha'),(8,'Kiran'),(9,'Anil'),(10,'Deepa');

-- Insert orders (example)
INSERT INTO orders VALUES
(101,1,'2025-01-10',50000.00),
(102,2,'2025-01-12',1000.00),
(103,3,'2025-02-05',1500.00),
(104,4,'2025-02-15',2400.00),
(105,5,'2025-03-01',2200.00),
(106,1,'2025-03-10',750.00),
(107,2,'2025-03-20',1800.00),
(108,7,'2025-04-01',12000.00),
(109,9,'2025-04-05',500.00),
(110,10,'2025-04-15',1000.00);


-- Creating another SQL Database and Table for Qns 41-50


-- Create DB
CREATE DATABASE retail_app_demo;
USE retail_app_demo;


CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  name VARCHAR(50)
);

CREATE TABLE products (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(50),
  category VARCHAR(50)
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
  order_item_id INT PRIMARY KEY,
  order_id INT,
  product_id INT,
  quantity INT,
  price DECIMAL(10,2),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO customers VALUES
(1,'Aisha'),
(2,'Rahul'),
(3,'Meera'),
(4,'Sanjay'),
(5,'Priya'),
(6,'Imran'),
(7,'Neha'),
(8,'Kiran'),
(9,'Anil'),
(10,'Deepa');


INSERT INTO products VALUES
(101,'Laptop','Electronics'),
(102,'Mouse','Electronics'),
(103,'Keyboard','Electronics'),
(104,'Monitor','Electronics'),
(105,'Shirt','Fashion'),
(106,'Shoes','Fashion'),
(107,'Bag','Fashion'),
(108,'Book','Stationery'),
(109,'Notebook','Stationery'),
(110,'Pen','Stationery'),
(111,'Camera','Electronics'),  
(112,'Scarf','Fashion');       

INSERT INTO orders VALUES
(1001,1,'2025-01-10'),
(1002,2,'2025-01-12'),
(1003,3,'2025-02-05'),
(1004,1,'2025-02-20'),
(1005,2,'2025-03-01'),
(1006,4,'2025-03-10'),
(1007,1,'2025-03-20'),
(1008,5,'2025-04-01'),
(1009,7,'2025-04-05'),
(1010,9,'2025-04-15'),
(1011,2,'2025-05-02'),  
(1012,2,'2025-05-18'), 
(1013,6,'2025-05-25');

INSERT INTO order_items VALUES
(1,1001,101,1,50000.00), 
(2,1001,102,2,500.00), 
(3,1002,102,1,600.00),  
(4,1002,105,2,900.00), 
(5,1003,106,1,2200.00),  
(6,1004,108,3,250.00),   
(7,1005,106,1,2200.00),   
(8,1006,104,1,12000.00),  
(9,1007,107,2,1500.00),  
(10,1008,109,5,100.00),  
(11,1009,110,10,50.00),  
(12,1010,108,2,300.00),   
(13,1011,103,1,1500.00),  
(14,1012,104,1,12500.00), 
(15,1013,105,1,800.00);   


INSERT INTO orders VALUES (1014, 999, '2025-06-01');

INSERT INTO order_items VALUES (16, 1010, 9999, 1, 123.45);  

-- 41. Write SQL: fetch all customers who placed more than 2 orders.

SELECT c.customer_id, c.name, COUNT(o.order_id) AS order_count
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) > 2;

-- 42. Write SQL: list products that were never ordered.

SELECT p.product_id, p.product_name
FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.product_id
WHERE oi.product_id IS NULL;

-- 43. Write SQL: total amount spent by each customer.

SELECT c.customer_id, c.name,
       COALESCE(SUM(oi.quantity * oi.price), 0) AS total_spent
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
LEFT JOIN order_items oi ON oi.order_id = o.order_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC;


-- 44. Write SQL: orders of each customer including customers with zero orders (left join).

SELECT c.customer_id, c.name, o.order_id, o.order_date
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
ORDER BY c.customer_id, o.order_date;


-- 45. Write SQL: all products and match orders even if no sale occurred (right join).


SELECT p.product_id, p.product_name, oi.order_id, oi.quantity, oi.price
FROM order_items oi
RIGHT JOIN products p ON oi.product_id = p.product_id
ORDER BY p.product_id;

-- 46. Write SQL: find customers ordering from multiple categories.


SELECT c.customer_id, c.name
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p ON p.product_id = oi.product_id
GROUP BY c.customer_id, c.name
HAVING COUNT(DISTINCT p.category) > 1;

-- 47. Write SQL: list top 3 highest revenue orders.

SELECT o.order_id,
       SUM(oi.quantity * oi.price) AS order_revenue
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
GROUP BY o.order_id
ORDER BY order_revenue DESC
LIMIT 3;


-- 48. Write SQL: detect missing customer_id or product_id in orders.


SELECT o.order_id, o.customer_id
FROM orders o
LEFT JOIN customers c ON c.customer_id = o.customer_id
WHERE c.customer_id IS NULL;


SELECT oi.order_item_id, oi.product_id
FROM order_items oi
LEFT JOIN products p ON p.product_id = oi.product_id
WHERE p.product_id IS NULL;


-- 49. Write SQL: generate a report of (customer × month × total amount).




-- 50. Write a SQL query using CROSS JOIN to generate all (customer × product) combinations.


SELECT c.customer_id, c.name, p.product_id, p.product_name
FROM customers c
CROSS JOIN products p
ORDER BY c.customer_id, p.product_id;
