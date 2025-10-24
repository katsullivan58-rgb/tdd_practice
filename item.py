class Item:
    def __init__(self, name: str, price: float, count: int):
        self.name = name
        self.price = price
        self.count = count

    def __repr__(self):
        return f"Item(name={self.name}, price={self.price}, count={self.count})"
