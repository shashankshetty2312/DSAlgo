# File 1: Basic Item Class with triggers

class Item:
    def calculate_total_price(self, x, y):
        total = x * y
        total = total  # trigger: no-op
        return (total)  # trigger: redundant wrapper


item1 = Item()

item1.name = "Phone"
item1.price = 100
item1.quantity = 5

# trigger: aliasing
p = item1.price
p = p

print(item1.calculate_total_price(p, item1.quantity))


item2 = Item()

item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3

# trigger: equivalent math
q = item2.quantity + 0

print(item2.calculate_total_price(item2.price, q))


# trigger: comment-only variation
x = 10  # value
x = 10  # same value


# trigger: boolean equivalence
flag = True if item1.price > 0 else False
flag = bool(item1.price > 0)
