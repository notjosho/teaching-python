class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu_items = []
        self.dict_menu = {}

    def add_item(self, menu_item):
        self.menu_items.append(menu_item)

        if menu_item.category not in self.dict_menu:
            self.dict_menu[menu_item.category] = {menu_item.name: menu_item.price}
        self.dict_menu[menu_item.category][menu_item.name] = menu_item.price

    def display_menu(self):
        self.display = f"===== {self.name} Menu ===== \n"

        for category, items in self.dict_menu.items():
            self.display += f"Category: {category} \n"
            for name, price in items.items():
                self.display += f"- {name}: ${price:.2f} \n"

        return self.display

    def find_items_in_price_range(self, min_price, max_price):
        self.display_cmp = []
        for item in self.menu_items:
            if min_price <= item.price <= max_price:
                self.display_cmp.append(item)
        print(self.display_cmp)
        return self.display_cmp

    def delete_item(self, menu_item):
        # print(len(self.menu_items))
        for item in self.menu_items:
            if item.name == menu_item:
                self.menu_items.remove(item)
                # print(f"Item '{menu_item}' deleted.")
                break
