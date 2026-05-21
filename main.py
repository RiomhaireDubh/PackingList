from packing_item import PackingItem

def main():
    # Create packing list items
    shirt = PackingItem("Shirt", 3)
    charger = PackingItem("Phone Charger", 1)
    snacks = PackingItem("Snacks", 5)

    print("Initial packing list:")
    print(shirt)
    print(charger)
    print(snacks)

    # Update values using the property setters
    shirt.quantity = 4
    snacks.name = "Trail Mix"

    print("\nUpdated packing list:")
    print(shirt)
    print(charger)
    print(snacks)

if __name__ == "__main__":
    main()
