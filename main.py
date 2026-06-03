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

    # Base packing list with weights (in pounds)
    items = [
        PackingItem("Shirt", 3, 0.4),
        PackingItem("Pants", 2, 1.0),
        PackingItem("Socks", 4, 0.1),
        PackingItem("Underwear", 4, 0.1),
        PackingItem("Jacket", 1, 1.5),

        PackingItem("Toothbrush", 1, 0.1),
        PackingItem("Toothpaste", 1, 0.2),
        PackingItem("Deodorant", 1, 0.3),
        PackingItem("Travel Shampoo", 1, 0.4),
        PackingItem("Soap", 1, 0.2),

        PackingItem("Phone Charger", 1, 0.2),
        PackingItem("Snacks", 5, 0.1),
        PackingItem("Water Bottle", 1, 0.5),
    ]

    # Add survival items if camping
    if trip_type.lower() == "camping":
        print("Camping trip detected — adding survival gear...\n")
        items.extend([
            PackingItem("Tent", 1, 5.0),
            PackingItem("Sleeping Bag", 1, 3.0),
            PackingItem("Fire Starter", 1, 0.2),
            PackingItem("Pocket Knife", 1, 0.3),
            PackingItem("Flashlight", 1, 0.4),
            PackingItem("Extra Batteries", 4, 0.1),
            PackingItem("First Aid Kit", 1, 1.0),
            PackingItem("Compass", 1, 0.1),
            PackingItem("Map", 1, 0.05),
            PackingItem("Rope / Paracord", 1, 0.7),
            PackingItem("Water Purification Tablets", 1, 0.1),
            PackingItem("Cooking Pot", 1, 1.2),
            PackingItem("Matches", 1, 0.05),
            PackingItem("Emergency Blanket", 1, 0.2),
        ])

    print("Initial packing list:")
    for item in items:
        print(item)

    # Update values using the property setters
    items[0].quantity = 4  # Increase shirt quantity
    items[11].name = "Trail Mix"  # Rename snacks

    print("\nUpdated packing list:")
    for item in items:
        print(item)

    # Calculate total weight
    total_weight = sum(item.total_weight() for item in items)
    print(f"\nTotal pack weight: {total_weight:.2f} lbs")

if __name__ == "__main__":
    main()
