from packing_item import PackingItem

def main():
    # Ask the user about their trip
    trip_type = input("What type of trip are you taking (vacation, business, camping, etc.): ")
    trip_length = input("How many days is your trip: ")
    travel_mode = input("How will you be traveling (car, plane, train, etc.): ")

    print("\nTrip Details:")
    print(f"Type of trip: {trip_type}")
    print(f"Length of trip: {trip_length} days")
    print(f"Mode of travel: {travel_mode}\n")

    # Create packing list items (clothing + bathroom necessities + essentials)
    shirt = PackingItem("Shirt", 3)
    pants = PackingItem("Pants", 2)
    socks = PackingItem("Socks", 4)
    underwear = PackingItem("Underwear", 4)
    jacket = PackingItem("Jacket", 1)

    toothbrush = PackingItem("Toothbrush", 1)
    toothpaste = PackingItem("Toothpaste", 1)
    deodorant = PackingItem("Deodorant", 1)
    shampoo = PackingItem("Travel Shampoo", 1)
    soap = PackingItem("Soap", 1)

    charger = PackingItem("Phone Charger", 1)
    snacks = PackingItem("Snacks", 5)
    water_bottle = PackingItem("Water Bottle", 1)

    print("Initial packing list:")
    print(shirt)
    print(pants)
    print(socks)
    print(underwear)
    print(jacket)
    print(toothbrush)
    print(toothpaste)
    print(deodorant)
    print(shampoo)
    print(soap)
    print(charger)
    print(snacks)
    print(water_bottle)

    # Update values using the property setters
    shirt.quantity = 4
    snacks.name = "Trail Mix"

    print("\nUpdated packing list:")
    print(shirt)
    print(pants)
    print(socks)
    print(underwear)
    print(jacket)
    print(toothbrush)
    print(toothpaste)
    print(deodorant)
    print(shampoo)
    print(soap)
    print(charger)
    print(water_bottle)
    print(snacks)

if __name__ == "__main__":
    main()
