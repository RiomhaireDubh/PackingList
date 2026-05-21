class PackingItem:
    def __init__(self, name, quantity=1):
        # protected attributes
        self._name = name
        self._quantity = quantity

    # getter for name
    @property
    def name(self):
        return self._name

    # setter for name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            print("Item name must be a non-empty string.")

    # getter for quantity
    @property
    def quantity(self):
        return self._quantity

    # setter for quantity
    @quantity.setter
    def quantity(self, new_qty):
        if isinstance(new_qty, int) and new_qty > 0:
            self._quantity = new_qty
        else:
            print("Quantity must be a positive integer.")

    def __str__(self):
        return f"{self._quantity} × {self._name}"
