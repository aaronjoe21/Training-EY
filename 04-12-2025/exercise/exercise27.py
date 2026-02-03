import json

with open("products.json", "r") as f:
    products = json.load(f)

for p in products:
    p["price"] *= 0.9  # 10% discount

with open("products.json", "w") as f:
    json.dump(products, f, indent=2)
