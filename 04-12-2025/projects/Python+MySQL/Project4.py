import csv, json, pymysql
from datetime import date

# --- Read product catalog from CSV ---
# catalog.csv: sku,name,price
catalog = {}
with open("catalog.csv") as f:
    for row in csv.DictReader(f):
        catalog[row["sku"]] = {"name": row["name"], "price": float(row["price"])}

# --- Read bill items from JSON ---
# bills.json: [{"sku":"A1","qty":2},{"sku":"B2","qty":1}]
with open("bills.json") as f:
    items = json.load(f)

# --- Compute totals ---
subtotal = 0.0
lines = []
for it in items:
    sku = it["sku"]
    qty = int(it["qty"])
    price = catalog[sku]["price"]
    line_total = qty * price
    subtotal += line_total
    lines.append({"sku": sku, "name": catalog[sku]["name"], "qty": qty, "price": price, "line_total": round(line_total,2)})

tax = round(subtotal * 0.18, 2)  # 18% GST example
grand_total = round(subtotal + tax, 2)

print("Subtotal:", round(subtotal,2), "Tax:", tax, "Grand:", grand_total)

# --- Save to MySQL: bill header + bill lines ---
conn = pymysql.connect(
    host="localhost",
    user="root",
    passwd="V@ishnav1",
    db="billing_db",   # create/use this DB
    autocommit=True
)
cur = conn.cursor()

# Tables (run once)
cur.execute("""
CREATE TABLE IF NOT EXISTS bills (
    bill_id INT PRIMARY KEY,
    bill_date DATE,
    subtotal DECIMAL(10,2),
    tax DECIMAL(10,2),
    grand_total DECIMAL(10,2)
)
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS bill_items (
    item_id INT PRIMARY KEY,
    bill_id INT,
    sku VARCHAR(50),
    name VARCHAR(100),
    qty INT,
    price DECIMAL(10,2),
    line_total DECIMAL(10,2)
)
""")

# Insert a new bill
bill_id = 1001  # simple fixed ID for demo; use AUTO_INCREMENT in real apps
cur.execute("INSERT IGNORE INTO bills (bill_id, bill_date, subtotal, tax, grand_total) VALUES (%s,%s,%s,%s,%s)",
            (bill_id, date.today(), round(subtotal,2), tax, grand_total))

# Insert lines
item_id_start = 1
for i, ln in enumerate(lines, start=item_id_start):
    cur.execute("""INSERT IGNORE INTO bill_items
                   (item_id, bill_id, sku, name, qty, price, line_total)
                   VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                (i, bill_id, ln["sku"], ln["name"], ln["qty"], ln["price"], ln["line_total"]))

# Verify save
cur.execute("SELECT * FROM bills WHERE bill_id=%s", (bill_id,))
print("Bill Header:", cur.fetchone())
cur.execute("SELECT sku, name, qty, price, line_total FROM bill_items WHERE bill_id=%s", (bill_id,))
for r in cur.fetchall():
    print("Line:", r)

cur.close()
conn.close()
