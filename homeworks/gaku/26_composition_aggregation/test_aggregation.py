# Test file for Aggregation Example
# Aggregation: Objects can exist independently and be shared between containers
from aggregation_example import MenuItem, Restaurant


def test_menuitem_init():
    """Test that MenuItem objects are created correctly with name, price, and category."""
    item = MenuItem(
        "Pizza",       # name
        12.99,         # price
        "Main Course"  # category
    )

    # MenuItem should store all provided attributes
    assert item.name == "Pizza", (
        "MenuItem.__init__ failed: Expected name to be 'Pizza', got '{}'".format(item.name)
    )
    assert item.price == 12.99, (
        "MenuItem.__init__ failed: Expected price to be 12.99, got {}".format(item.price)
    )
    assert item.category == "Main Course", (
        "MenuItem.__init__ failed: Expected category to be 'Main Course', got '{}'".format(item.category)
    )


def test_restaurant_init():
    """Test that Restaurant objects are created with an empty menu."""
    restaurant = Restaurant("Test Restaurant")

    # New restaurant should have a name but no menu items yet
    assert restaurant.name == "Test Restaurant", (
        "Restaurant.__init__ failed: Expected name to be 'Test Restaurant', got '{}'".format(restaurant.name)
    )
    assert restaurant.menu_items == [], (
        "Restaurant.__init__ failed: Expected menu_items to be empty list, got {}".format(restaurant.menu_items)
    )


def test_restaurant_add_item():
    """Test that items can be added to a restaurant's menu."""
    restaurant = Restaurant("Test Restaurant")
    item = MenuItem(
        "Burger",      # name
        8.50,          # price
        "Main Course"  # category
    )

    restaurant.add_item(item)

    # Restaurant should now contain exactly one item - the one we added
    assert len(restaurant.menu_items) == 1, (
        "Restaurant.add_item failed: Expected 1 item in menu_items, got {}".format(len(restaurant.menu_items))
    )
    assert restaurant.menu_items[0] == item, (
        "Restaurant.add_item failed: Expected the added item to be in menu_items"
    )


def test_restaurant_display_menu():
    """Test that display_menu returns a properly formatted menu string with categories."""
    restaurant = Restaurant("Gaku Restaurant")

    # Add items from different categories
    restaurant.add_item(MenuItem("Pizza", 12.99, "Main Course"))
    restaurant.add_item(MenuItem("Salad", 8.50, "Appetizer"))
    restaurant.add_item(MenuItem("Pasta", 11.99, "Main Course"))

    menu_string = restaurant.display_menu()

    # Should return a string containing the restaurant name header
    assert isinstance(menu_string, str), (
        "Restaurant.display_menu failed: Expected return type str, got {}".format(type(menu_string).__name__)
    )
    assert "===== Gaku Restaurant Menu =====" in menu_string, (
        "Restaurant.display_menu failed: Expected restaurant name header in output"
    )

    # Should have category labels
    assert "Category: Main Course" in menu_string, (
        "Restaurant.display_menu failed: Expected 'Category: Main Course' in output"
    )
    assert "Category: Appetizer" in menu_string, (
        "Restaurant.display_menu failed: Expected 'Category: Appetizer' in output"
    )

    # Items should be formatted with dash prefix and price
    assert "- Pizza: $12.99" in menu_string, (
        "Restaurant.display_menu failed: Expected '- Pizza: $12.99' in output"
    )
    assert "- Salad: $8.50" in menu_string, (
        "Restaurant.display_menu failed: Expected '- Salad: $8.50' in output"
    )
    assert "- Pasta: $11.99" in menu_string, (
        "Restaurant.display_menu failed: Expected '- Pasta: $11.99' in output"
    )

    # Verify items appear under correct categories by checking order in string
    main_course_pos = menu_string.find("Category: Main Course")
    appetizer_pos = menu_string.find("Category: Appetizer")
    pizza_pos = menu_string.find("Pizza")
    pasta_pos = menu_string.find("Pasta")
    salad_pos = menu_string.find("Salad")

    # Pizza and Pasta should appear after Main Course category
    assert main_course_pos < pizza_pos, (
        "Restaurant.display_menu failed: Expected 'Pizza' to appear after 'Category: Main Course'"
    )
    assert main_course_pos < pasta_pos, (
        "Restaurant.display_menu failed: Expected 'Pasta' to appear after 'Category: Main Course'"
    )

    # Salad should appear after Appetizer category
    assert appetizer_pos < salad_pos, (
        "Restaurant.display_menu failed: Expected 'Salad' to appear after 'Category: Appetizer'"
    )


def test_aggregation_shared_items():
    """Test that the same MenuItem can belong to multiple restaurants (key aggregation behavior)."""
    restaurant1 = Restaurant("Restaurant 1")
    restaurant2 = Restaurant("Restaurant 2")

    # Create ONE item and add to BOTH restaurants
    shared_item = MenuItem(
        "Pasta",       # name
        9.99,          # price
        "Main Course"  # category
    )
    restaurant1.add_item(shared_item)
    restaurant2.add_item(shared_item)

    # Both restaurants should have the item
    assert len(restaurant1.menu_items) == 1, (
        "Aggregation (shared items) failed: Expected restaurant1 to have 1 item, got {}".format(len(restaurant1.menu_items))
    )
    assert len(restaurant2.menu_items) == 1, (
        "Aggregation (shared items) failed: Expected restaurant2 to have 1 item, got {}".format(len(restaurant2.menu_items))
    )

    # Crucially: they should reference the SAME object (not copies)
    assert restaurant1.menu_items[0] is restaurant2.menu_items[0], (
        "Aggregation (shared items) failed: Expected both restaurants to reference the SAME MenuItem object"
    )


def test_aggregation_shared_references():
    """Test that modifying a shared item affects all restaurants containing it."""
    restaurant1 = Restaurant("Restaurant 1")
    restaurant2 = Restaurant("Restaurant 2")

    # Share the same item between restaurants
    item = MenuItem(
        "Salad",     # name
        7.50,        # price
        "Appetizer"  # category
    )
    restaurant1.add_item(item)
    restaurant2.add_item(item)

    # Modify the item's price
    item.price = 9.99

    # Both restaurants should see the new price (shared reference)
    assert restaurant1.menu_items[0].price == 9.99, (
        "Aggregation (shared references) failed: Expected restaurant1 item price to be 9.99 after modification, got {}".format(
            restaurant1.menu_items[0].price
        )
    )
    assert restaurant2.menu_items[0].price == 9.99, (
        "Aggregation (shared references) failed: Expected restaurant2 item price to be 9.99 after modification, got {}".format(
            restaurant2.menu_items[0].price
        )
    )


def test_restaurant_find_items_in_price_range():
    """Test filtering items by price range (min and max inclusive)."""
    restaurant = Restaurant("Test Restaurant")

    # Add items with varying prices
    item1 = MenuItem("Item1", 5.00, "Appetizer")    # In range: $5-$12
    item2 = MenuItem("Item2", 10.00, "Main Course") # In range: $5-$12
    item3 = MenuItem("Item3", 15.00, "Main Course") # Out of range: too expensive
    item4 = MenuItem("Item4", 3.00, "Beverage")     # Out of range: too cheap

    restaurant.add_item(item1)
    restaurant.add_item(item2)
    restaurant.add_item(item3)
    restaurant.add_item(item4)

    # Filter for items between $5.00 and $12.00
    filtered = restaurant.find_items_in_price_range(
        5.00,   # min_price (inclusive)
        12.00   # max_price (inclusive)
    )

    # Should find exactly 2 items within range
    assert len(filtered) == 2, (
        "Restaurant.find_items_in_price_range failed: Expected 2 items in range $5-$12, got {}".format(len(filtered))
    )
    assert item1 in filtered, (
        "Restaurant.find_items_in_price_range failed: Expected Item1 ($5.00) to be in range $5-$12 (lower boundary)"
    )
    assert item2 in filtered, (
        "Restaurant.find_items_in_price_range failed: Expected Item2 ($10.00) to be in range $5-$12 (middle)"
    )
    assert item3 not in filtered, (
        "Restaurant.find_items_in_price_range failed: Expected Item3 ($15.00) to NOT be in range $5-$12 (above range)"
    )
    assert item4 not in filtered, (
        "Restaurant.find_items_in_price_range failed: Expected Item4 ($3.00) to NOT be in range $5-$12 (below range)"
    )


def test_restaurant_add_item_multiple_categories():
    """Test that a restaurant can hold multiple items from different categories."""
    restaurant = Restaurant("Test Restaurant")

    # Add items from four different categories
    items = [
        MenuItem("Appetizer1", 5.00, "Appetizer"),
        MenuItem("Main1", 12.00, "Main Course"),
        MenuItem("Dessert1", 7.00, "Dessert"),
        MenuItem("Beverage1", 3.00, "Beverage"),
    ]

    for item in items:
        restaurant.add_item(item)

    # Restaurant should contain all 4 items
    assert len(restaurant.menu_items) == 4, (
        "Restaurant.add_item (multiple categories) failed: Expected 4 items, got {}".format(len(restaurant.menu_items))
    )


def test_menuitem_independent_existence():
    """Test that MenuItems can exist without belonging to any restaurant (aggregation property)."""
    # Create item without adding to any restaurant
    item = MenuItem(
        "Independent Item",  # name
        10.00,               # price
        "Main Course"        # category
    )

    # Item exists and has valid properties on its own
    assert item.name == "Independent Item", (
        "MenuItem (independent existence) failed: Expected name 'Independent Item', got '{}'".format(item.name)
    )
    assert item.price == 10.00, (
        "MenuItem (independent existence) failed: Expected price 10.00, got {}".format(item.price)
    )

    # Item can be added to a restaurant later
    restaurant = Restaurant("Test")
    restaurant.add_item(item)

    # Item still maintains its identity
    assert item.name == "Independent Item", (
        "MenuItem (independent existence) failed: Expected item to maintain identity after adding to restaurant"
    )


def test_restaurant_delete_item():
    """Test that delete_item removes item from one restaurant without affecting others."""
    restaurant1 = Restaurant("Restaurant 1")
    restaurant2 = Restaurant("Restaurant 2")

    # Create shared items
    item1 = MenuItem("Pasta", 12.00, "Main Course")
    item2 = MenuItem("Salad", 8.00, "Appetizer")

    # Add both items to both restaurants
    restaurant1.add_item(item1)
    restaurant1.add_item(item2)
    restaurant2.add_item(item1)
    restaurant2.add_item(item2)

    # Delete Salad from restaurant1 only
    restaurant1.delete_item("Salad")

    # Restaurant1 should only have Pasta now
    assert len(restaurant1.menu_items) == 1, (
        "Restaurant.delete_item failed: Expected restaurant1 to have 1 item after deletion, got {}".format(
            len(restaurant1.menu_items)
        )
    )
    assert item1 in restaurant1.menu_items, (
        "Restaurant.delete_item failed: Expected 'Pasta' to remain in restaurant1"
    )
    assert item2 not in restaurant1.menu_items, (
        "Restaurant.delete_item failed: Expected 'Salad' to be removed from restaurant1"
    )

    # Restaurant2 should still have BOTH items (aggregation: independent references)
    assert len(restaurant2.menu_items) == 2, (
        "Restaurant.delete_item failed: Expected restaurant2 to still have 2 items (aggregation), got {}".format(
            len(restaurant2.menu_items)
        )
    )
    assert item1 in restaurant2.menu_items, (
        "Restaurant.delete_item failed: Expected 'Pasta' to remain in restaurant2"
    )
    assert item2 in restaurant2.menu_items, (
        "Restaurant.delete_item failed: Expected 'Salad' to remain in restaurant2 (aggregation: deletion in one restaurant should not affect others)"
    )

    # The deleted item still exists in memory (not destroyed)
    assert item2.name == "Salad", (
        "Restaurant.delete_item failed: Expected deleted item to still exist in memory (aggregation property)"
    )


if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("Running Aggregation Tests")
    print("=" * 50 + "\n")

    test_menuitem_init()
    print("[PASSED] MenuItem.__init__")

    test_restaurant_init()
    print("[PASSED] Restaurant.__init__")

    test_restaurant_add_item()
    print("[PASSED] Restaurant.add_item")

    test_restaurant_display_menu()
    print("[PASSED] Restaurant.display_menu")

    test_aggregation_shared_items()
    print("[PASSED] Aggregation: shared items between restaurants")

    test_aggregation_shared_references()
    print("[PASSED] Aggregation: shared references")

    test_restaurant_find_items_in_price_range()
    print("[PASSED] Restaurant.find_items_in_price_range")

    test_restaurant_add_item_multiple_categories()
    print("[PASSED] Restaurant.add_item (multiple categories)")

    test_menuitem_independent_existence()
    print("[PASSED] MenuItem: independent existence")

    test_restaurant_delete_item()
    print("[PASSED] Restaurant.delete_item")

    print("\n" + "=" * 50)
    print("All aggregation tests passed!")
    print("=" * 50)
