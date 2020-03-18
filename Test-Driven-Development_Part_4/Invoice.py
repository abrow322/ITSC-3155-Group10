class Invoice:
    def __init__(self):
        self.items = {}

    def addProducts(self, qnt, price, discount):
        self.items['qnt'] = qnt
        self.items['unit price'] = price
        self.items['discount'] = discount
        return self.items

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v['unit price']) * int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price

    def totalDiscount(self, products):
        total_discount = 0
        for k, v in products.items():
            total_discount += (int(v['qnt']) * float(v['unit price'])) * float(v['discount']) / 100
        total_discount = round(total_discount, 2)
        self.total_discount = total_discount
        return total_discount

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products)-self.totalDiscount(products)
        return total_pure_price

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['v', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput

    def totalTime(self, products, delivery_type):
        total_time = 0
        time_per_unit = delivery_type
        if delivery_type == 3:  # checks for 1 day override
            total_time = 1
        else:   # otherwise calculates time per unit
            for k, v in products.items():
                total_time += (int(v['qnt'])) * time_per_unit

        self.total_time = total_time
        return total_time

    def deliveryType(self, input_value):
        while True:         # determines time per unit, or 1 day shipping if selected
            userInput = input_value # receives users choice
            if userInput == 1:
                return 2    # days per product
            elif userInput == 2:
                return 1    # one day shipping per product
            elif userInput == 3:
                return 3    # 1 day override; value not per product
            else:
                print("Not a valid number")
