class PackingItem:
    def __init__(self, name, quantity=1, weight=0):
        self._name = name
        self._quantity = quantity
        self._weight = weight  # weight of ONE unit

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            print("Item name must be a non-empty string.")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, new_qty):
        if isinstance(new_qty, int) and new_qty > 0:
            self._quantity = new_qty
        else:
            print("Quantity must be a positive integer.")

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        if isinstance(new_weight, (int, float)) and new_weight >= 0:
            self._weight = new_weight
        else:
            print("Weight must be a non-negative number.")

    def total_weight(self):
        return self._quantity * self._weight

    def __str__(self):
        return f"{self._quantity} × {self._name} ({self.total_weight():.2f} lbs)"
