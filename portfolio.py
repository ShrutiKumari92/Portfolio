import csv
import stockprices


portfolio = {}

n= int(input("enter no of stocks that you own want : "))
for i in range(n):
    stockname = input("enter stock name : ").upper()
    if stockname not in stockprices.stock_price:
        i-=1
        print("your stock name not listed here. Please try again : ")
        
        continue
        
    quantity = int(input("enter quantity that you own want : "))
    portfolio[stockname]=quantity

investment =0
for stockname,quantity in portfolio.items():
    price=stockprices.stock_price[stockname]
    invest = price*quantity
    investment+=invest

print(f'your total investment of stocks is {investment}')
save = input("Do you want to save this portfolio in file?(Yes/No) : ").lower()
if save=="yes":
    filename=input("enter your file type  (txt/csv) :").lower()
    if filename=='txt':
        with open("portfolio.txt","w") as f:
            for stockname,quantity in portfolio.items():

                f.write(f"you invest {stockname} with quantity {quantity}  \n")
            f.write(f'your total investment is Rs {investment}')
        print("✅ Portfolio saved as portfolio.txt")
    elif filename=='csv':
        with open("portfolio.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Stock", "Quantity", "Price", "Investment"])
                for stockname, quantity in portfolio.items():
                    writer.writerow([stockname, quantity, stockprices.stock_price[stockname], stockprices.stock_price[stockname] * quantity])
                writer.writerow(["TOTAL", "", "", investment])
        print("✅ Portfolio saved as portfolio.csv") 
    else:
        print("❌invalid file type. I am not able to save !!!")