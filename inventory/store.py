from inventory.config import MAX_ITEMS, LOW_STOCK


class Store:
    def __init__(self):
        self.items = {}

    def add(self, name, qty):
        if len(self.items) >= MAX_ITEMS and name not in self.items:
            raise ValueError("store full")
        self.items[name] = self.items.get(name, 0) + qty

    def get_count(self, name):
        return self.items.get(name, 0)

    def low_stock(self):
        return sorted(n for n, q in self.items.items() if q < LOW_STOCK)
