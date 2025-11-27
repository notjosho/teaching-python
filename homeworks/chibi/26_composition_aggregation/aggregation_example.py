class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu_items = []

    def add_item(self, menu_item):
        self.menu_items.append(menu_item)

    def display_menu(self):
        output = f"===== {self.name} Menu =====\n\n"
        categories = {}

        for item in self.menu_items:
            if item.category not in categories:
                categories[item.category] = []
            categories[item.category].append(item)

        for category, items in categories.items():
            output += f"Category: {category}\n"
            for item in items:
                output += f"- {item.name}: ${item.price:.2f}\n"
            output += "\n"

        print(output)
        return output

    def find_items_in_price_range(self, min_price, max_price):
        return [
            item for item in self.menu_items if min_price <= item.price <= max_price
        ]

    def delete_item(self, item_name):
        self.menu_items = [item for item in self.menu_items if item.name != item_name]
