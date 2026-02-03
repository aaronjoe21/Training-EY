import csv
total=0
sum1=0
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        with open("invoices.txt", "a+") as c:
            total=int(row["Quantity"])*int(row["Price"])
            sum1+=total
            c.write(f"""
                --------------------
                Item: {row["Item"]}
                Price: {(row["Price"])}
                Quantity: {(row["Quantity"])}
                Total: {total}
                --------------------""")
with open("invoices.txt", "a") as c:
    c.write(f"Sum of Total: {sum1}")