# ------------------------------------------------------------
# PROGRAM: main.py
# PURPOSE: Packing list generator
# AUTHOR:  Brian Lewis
# DATE:    06/07/2026
# ------------------------------------------------------------


from packing_item import PackingItem

# -----------------------------------------
# CATEGORY DEFINITIONS
# -----------------------------------------
CATEGORIES = {
    "Clothing": [],
    "Hygiene": [],
    "Electronics": [],
    "Food": [],
    "Survival": [],
    "Motorcycle Gear": [],
    "Misc": []
}

# -----------------------------------------
# BASE ITEMS
# -----------------------------------------
def load_base_items():
    CATEGORIES["Clothing"].extend([
        PackingItem("Shirt", 3, 0.4),
        PackingItem("Pants", 2, 1.0),
        PackingItem("Socks", 4, 0.1),
        PackingItem("Underwear", 4, 0.1),
        PackingItem("Jacket", 1, 1.5),
    ])

    CATEGORIES["Hygiene"].extend([
        PackingItem("Toothbrush", 1, 0.1),
        PackingItem("Toothpaste", 1, 0.2),
        PackingItem("Deodorant", 1, 0.3),
        PackingItem("Travel Shampoo", 1, 0.4),
        PackingItem("Soap", 1, 0.2),
    ])

    CATEGORIES["Electronics"].append(PackingItem("Phone Charger", 1, 0.2))

    CATEGORIES["Food"].extend([
        PackingItem("Snacks", 5, 0.1),
        PackingItem("Water Bottle", 1, 0.5),
    ])


# -----------------------------------------
# CAMPING ITEMS
# -----------------------------------------
def add_camping_items():
    CATEGORIES["Survival"].extend([
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


# -----------------------------------------
# MOTORCYCLE ITEMS
# -----------------------------------------
def add_motorcycle_items():
    CATEGORIES["Motorcycle Gear"].extend([
        PackingItem("Motorcycle Helmet", 1, 3.5),
        PackingItem("Riding Gloves", 1, 0.4),
        PackingItem("Motorcycle Jacket (Armored)", 1, 5.0),
        PackingItem("Rain Gear", 1, 1.2),
        PackingItem("Tool Kit", 1, 2.0),
        PackingItem("Tire Repair Kit", 1, 1.0),
        PackingItem("Portable Air Pump", 1, 1.5),
        PackingItem("Bungee Cords / Straps", 1, 0.8),
        PackingItem("Chain Lube", 1, 0.5),
        PackingItem("Earplugs", 1, 0.05),
        PackingItem("Spare Gloves", 1, 0.3),
    ])


# -----------------------------------------
# WEATHER-BASED ITEMS
# -----------------------------------------
def add_weather_items(weather):
    weather = weather.lower()

    if "hot" in weather or "warm" in weather:
        CATEGORIES["Clothing"].extend([
            PackingItem("Shorts", 2, 0.3),
            PackingItem("Sun Hat", 1, 0.2),
        ])
        CATEGORIES["Hygiene"].append(PackingItem("Sunscreen", 1, 0.5))
        CATEGORIES["Misc"].append(PackingItem("Cooling Towel", 1, 0.2))

    if "cold" in weather or "freezing" in weather:
        CATEGORIES["Clothing"].extend([
            PackingItem("Thermal Shirt", 2, 0.4),
            PackingItem("Thermal Pants", 1, 0.5),
            PackingItem("Beanie", 1, 0.2),
            PackingItem("Gloves", 1, 0.2),
        ])
        CATEGORIES["Survival"].append(PackingItem("Hand Warmers", 4, 0.05))

    if "rain" in weather or "wet" in weather:
        CATEGORIES["Clothing"].append(PackingItem("Rain Jacket", 1, 1.0))
        CATEGORIES["Misc"].append(PackingItem("Waterproof Bag Cover", 1, 0.3))
        CATEGORIES["Misc"].append(PackingItem("Umbrella", 1, 0.7))

    if "snow" in weather or "blizzard" in weather:
        CATEGORIES["Clothing"].extend([
            PackingItem("Snow Boots", 1, 3.0),
            PackingItem("Heavy Coat", 1, 3.5),
        ])
        CATEGORIES["Survival"].append(PackingItem("Ice Scraper", 1, 0.4))

    if "wind" in weather or "gust" in weather:
        CATEGORIES["Clothing"].append(PackingItem("Windbreaker", 1, 0.6))


# -----------------------------------------
# AUTO-ADJUST QUANTITIES
# -----------------------------------------
def auto_adjust_quantities(days):
    for category, items in CATEGORIES.items():
        for item in items:
            if item.name in ["Shirt", "Socks", "Underwear"]:
                item.quantity = max(1, days)
            if item.name == "Pants":
                item.quantity = max(1, days // 2)


def auto_adjust_weather(weather):
    weather = weather.lower()

    for category, items in CATEGORIES.items():
        for item in items:
            if "hot" in weather and item.name == "Water Bottle":
                item.quantity = max(item.quantity, 2)

            if "cold" in weather and item.name == "Jacket":
                item.quantity = max(item.quantity, 2)

            if "rain" in weather and item.name == "Rain Jacket":
                item.quantity = 1

            if "snow" in weather and item.name in ["Gloves", "Beanie"]:
                item.quantity = max(item.quantity, 1)


# -----------------------------------------
# MENU SYSTEM
# -----------------------------------------
def show_menu():
    print("\n--- Packing List Menu ---")
    print("1. View packing list")
    print("2. Add item")
    print("3. Remove item")
    print("4. Change quantity")
    print("5. Change weight")
    print("6. Show total weight")
    print("7. Toggle packed/unpacked")
    print("8. Quit")


def choose_category():
    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES.keys(), start=1):
        print(f"{i}. {cat}")

    choice = input("Choose a category number: ")
    try:
        return list(CATEGORIES.keys())[int(choice) - 1]
    except:
        print("Invalid category.")
        return None


def view_list():
    print("\n--- PACKING LIST ---")
    for category, items in CATEGORIES.items():
        print(f"\n{category}:")
        if not items:
            print("  (empty)")
        for item in items:
            print("  " + str(item))


def add_item():
    category = choose_category()
    if not category:
        return

    name = input("Item name: ")
    qty = int(input("Quantity: "))
    weight = float(input("Weight per unit: "))

    CATEGORIES[category].append(PackingItem(name, qty, weight))
    print(f"Added {qty} × {name} to {category}")


def remove_item():
    category = choose_category()
    if not category:
        return

    items = CATEGORIES[category]
    if not items:
        print("No items in this category.")
        return

    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")

    choice = int(input("Choose item number to remove: "))
    try:
        removed = items.pop(choice - 1)
        print(f"Removed {removed.name}")
    except:
        print("Invalid choice.")


def change_quantity():
    category = choose_category()
    if not category:
        return

    items = CATEGORIES[category]
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")

    choice = int(input("Choose item number: "))
    new_qty = int(input("New quantity: "))

    try:
        items[choice - 1].quantity = new_qty
    except:
        print("Invalid choice.")


def change_weight():
    category = choose_category()
    if not category:
        return

    items = CATEGORIES[category]
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")

    choice = int(input("Choose item number: "))
    new_weight = float(input("New weight per unit: "))

    try:
        items[choice - 1].weight = new_weight
    except:
        print("Invalid choice.")


def toggle_packed():
    category = choose_category()
    if not category:
        return

    items = CATEGORIES[category]
    if not items:
        print("No items in this category.")
        return

    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")

    choice = int(input("Choose item number to toggle packed: "))
    try:
        items[choice - 1].toggle_packed()
        print(f"Toggled packed state for {items[choice - 1].name}")
    except:
        print("Invalid choice.")


def show_total_weight():
    total = 0
    for items in CATEGORIES.values():
        for item in items:
            total += item.total_weight()
    print(f"\nTotal pack weight: {total:.2f} lbs")


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------
def main():
    trip_type = input("Trip type (vacation, business, camping, etc.): ")
    trip_length = int(input("Trip length in days: "))
    travel_mode = input("Travel mode (car, plane, motorcycle, etc.): ")
    weather = input("Expected weather (hot, cold, rain, snow, wind, etc.): ")

    load_base_items()

    if trip_type.lower() == "camping":
        add_camping_items()

    if travel_mode.lower() == "motorcycle":
        add_motorcycle_items()

    add_weather_items(weather)
    auto_adjust_quantities(trip_length)
    auto_adjust_weather(weather)

    # MENU LOOP
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_list()
        elif choice == "2":
            add_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            change_quantity()
        elif choice == "5":
            change_weight()
        elif choice == "6":
            show_total_weight()
        elif choice == "7":
            toggle_packed()
        elif choice == "8":
            print("Good luck on your trip!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
