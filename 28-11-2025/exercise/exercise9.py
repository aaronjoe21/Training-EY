f=open("order_summary.txt","w")
b='''
--------------------------------
        ORDER SUMMARY
--------------------------------
'''
f.write(b)
f.close()
sum=0
def order(name,quantity,price):
    global sum
    total=quantity*price
    sum+=total
    f=open("order_summary.txt","a")
    a=f'''
    PRODUCT NAME: {name}
    QUANTITY: {quantity}
    PRICE: {price}
    TOTAL: {total}
    ----------------------------------
    '''
    f.write(a)
    f.close()



while True:
    n = input("DO YOU WANT TO ADD:")
    if n=="YES":
        name=input("Enter item name:")
        quantity=int(input("Enter quantity:"))
        price=float(input("Enter price:"))
        order(name,quantity,price)
    elif n=="NO":
        f=open("order_summary.txt","a")
        f.write(f"TOTAL SUM: {sum}")
        break
