from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
total_time = 0
delivery_type = 0
while True:
    product = input('What is your product : ')
    unit_price = Invoice().inputNumber("Please enter unit price : ")
    qnt = Invoice().inputNumber("Please enter quantity of product : ")
    discount = Invoice().inputNumber("Discount percent (%) : ")
    repeat = Invoice().inputAnswer("Another product? (y,n) : ")
    result = Invoice().addProduct(qnt, unit_price, discount)
    products[product] = result
    if repeat == "n":
        break

total_amount = Invoice().totalPurePrice(products)

print("Delivery Types: \n 1. Normal Delivery\n 2. Express Delivery\n 3. 1- day Shipping")
delivery_type = int(input("Enter Delivery Type : "))

delivery_time = Invoice().deliveryType(delivery_type)

total_time = Invoice().totalTime(products, delivery_time) #calculate total time

print("Your total pure price is: ", total_amount)

print("Total time for delivery is {0} day(s)".format(total_time)) #print total time