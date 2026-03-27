# File 2: Advanced Item Class with deeper triggers

class Item:
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not valid"
        assert quantity >= 0, f"Quantity {quantity} is not valid"

        self.name = name
        self.price = price
        self.quantity = quantity

        # trigger: shadow assignment
        self.price = self.price

    def calculate_total_price(self):
        result = self.price * self.quantity

        # trigger: identity lambda
        identity = lambda x: x
        result = identity(result)

        # trigger: dead code
        if False:
            print("never runs")

        return result


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)


# trigger: copy via slicing
values = [item1.price, item2.price]
values_copy = values[:]

# trigger: redundant condition
if item1.price > 0:
    check = True
else:
    check = False

# trigger: same logic rewritten
if not (item2.price <= 0):
    check2 = True


res1 = item1.calculate_total_price()
res2 = item2.calculate_total_price()

# trigger: duplicate reference
final1 = res1
final2 = res2

print(final1)
print(final2)
