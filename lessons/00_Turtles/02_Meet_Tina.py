#this program is called The Best Discount. You can input discounts you get and you can edit the discounts by modding this program.


#These are variables. 
fixedDiscount = float(input("Enter a fixed discount: "))
percentDiscount = float(input("Enter a percent disount: "))
price = float(input("Enter the price: "))
shippingCost = float(input("Enter the shipping cost: "))
actualShippingCost = float(price + shippingCost)

#These are the APPLIED variables.
actualPercentDiscount = float(percentDiscount / 100)
actualFixedDiscount = float(price - fixedDiscount)
shippingDiscount = float(price)

#This calculates the better discount.
if actualPercentDiscount < actualFixedDiscount and shippingDiscount:
    print("Use the percentage discount")

if actualFixedDiscount < actualPercentDiscount and shippingDiscount:
    print("Use the fixed discount")

if shippingDiscount < actualFixedDiscount and actualPercentDiscount:
    print("Use the shipping discount")
