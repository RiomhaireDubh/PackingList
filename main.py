from packing_item import PackingItem

def main():
    # Ask the user about the trip
    days = input("How many days is your trip: ")
    weather = input("What will the weather be like on your trip: ")

    print(f"\nTrip length: {days} days")
    print(f"Expected weather: {weather}\n")

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
