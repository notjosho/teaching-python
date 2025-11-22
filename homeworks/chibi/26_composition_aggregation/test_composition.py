# Test file for Composition Example
# Composition: Parent object owns and creates child objects (children don't exist independently)
from composition_example import Battery, Processor, Smartphone


def test_battery_init():
    """Test that Battery objects are created with capacity and full charge."""
    battery = Battery(3000)  # 3000mAh battery

    # Battery should store capacity and start fully charged
    assert battery.capacity == 3000, (
        "Battery.__init__ failed: Expected capacity to be 3000, got {}".format(battery.capacity)
    )
    assert battery.charge_level == 100, (
        "Battery.__init__ failed: Expected charge_level to be 100 (fully charged), got {}".format(battery.charge_level)
    )


def test_processor_init():
    """Test that Processor objects store model name and speed."""
    processor = Processor(
        "A15 Bionic",  # model
        3.2            # speed in GHz
    )

    assert processor.model == "A15 Bionic", (
        "Processor.__init__ failed: Expected model to be 'A15 Bionic', got '{}'".format(processor.model)
    )
    assert processor.speed == 3.2, (
        "Processor.__init__ failed: Expected speed to be 3.2, got {}".format(processor.speed)
    )


def test_smartphone_init():
    """Test that Smartphone creates and owns its Battery and Processor (composition)."""
    phone = Smartphone(
        "Apple",       # brand
        "iPhone 14",   # model
        3279,          # battery_capacity
        "A15 Bionic",  # processor_model
        3.2            # processor_speed
    )

    # Phone should have brand and model
    assert phone.brand == "Apple", (
        "Smartphone.__init__ failed: Expected brand to be 'Apple', got '{}'".format(phone.brand)
    )
    assert phone.model == "iPhone 14", (
        "Smartphone.__init__ failed: Expected model to be 'iPhone 14', got '{}'".format(phone.model)
    )

    # Composition: Phone CREATES its own Battery and Processor internally
    assert isinstance(phone.battery, Battery), (
        "Smartphone.__init__ failed: Expected phone.battery to be a Battery instance, got {}".format(
            type(phone.battery).__name__
        )
    )
    assert isinstance(phone.processor, Processor), (
        "Smartphone.__init__ failed: Expected phone.processor to be a Processor instance, got {}".format(
            type(phone.processor).__name__
        )
    )


def test_smartphone_init_owns_battery():
    """Test that Smartphone creates Battery with correct capacity (composition)."""
    phone = Smartphone(
        "Apple",       # brand
        "iPhone 14",   # model
        3279,          # battery_capacity (iPhone 14 battery)
        "A15 Bionic",  # processor_model
        3.2            # processor_speed
    )

    # Battery should be created INSIDE smartphone with the given capacity
    assert phone.battery is not None, (
        "Smartphone.__init__ (owns Battery) failed: Expected phone.battery to not be None"
    )
    assert phone.battery.capacity == 3279, (
        "Smartphone.__init__ (owns Battery) failed: Expected battery capacity to be 3279, got {}".format(
            phone.battery.capacity
        )
    )
    assert phone.battery.charge_level == 100, (
        "Smartphone.__init__ (owns Battery) failed: Expected battery to start fully charged (100%), got {}".format(
            phone.battery.charge_level
        )
    )


def test_smartphone_init_owns_processor():
    """Test that Smartphone creates Processor with correct specs (composition)."""
    phone = Smartphone(
        "Samsung",            # brand
        "Galaxy S23",         # model
        3900,                 # battery_capacity
        "Snapdragon 8 Gen 2", # processor_model
        3.4                   # processor_speed
    )

    # Processor should be created INSIDE smartphone with given model and speed
    assert phone.processor is not None, (
        "Smartphone.__init__ (owns Processor) failed: Expected phone.processor to not be None"
    )
    assert phone.processor.model == "Snapdragon 8 Gen 2", (
        "Smartphone.__init__ (owns Processor) failed: Expected processor model 'Snapdragon 8 Gen 2', got '{}'".format(
            phone.processor.model
        )
    )
    assert phone.processor.speed == 3.4, (
        "Smartphone.__init__ (owns Processor) failed: Expected processor speed 3.4, got {}".format(
            phone.processor.speed
        )
    )


def test_composition_independent_components():
    """Test that each smartphone has its OWN battery and processor (not shared)."""
    phone1 = Smartphone("Apple", "iPhone 14", 3279, "A15 Bionic", 3.2)
    phone2 = Smartphone("Samsung", "Galaxy S23", 3900, "Snapdragon 8 Gen 2", 3.4)

    # Each phone should have DIFFERENT battery and processor objects
    assert phone1.battery is not phone2.battery, (
        "Composition (independent components) failed: Expected phone1 and phone2 to have different Battery objects"
    )
    assert phone1.processor is not phone2.processor, (
        "Composition (independent components) failed: Expected phone1 and phone2 to have different Processor objects"
    )

    # Modifying phone1's battery should NOT affect phone2
    phone1.battery.charge_level = 50
    assert phone2.battery.charge_level == 100, (
        "Composition (independent components) failed: Expected phone2 battery to remain at 100% after modifying phone1, got {}%".format(
            phone2.battery.charge_level
        )
    )


def test_smartphone_get_specs():
    """Test that get_specs returns formatted string with all phone information."""
    phone = Smartphone("Apple", "iPhone 14", 3279, "A15 Bionic", 3.2)
    specs = phone.get_specs()

    # Specs should include brand, model, processor info, and battery info
    assert "Apple" in specs, (
        "Smartphone.get_specs failed: Expected 'Apple' in specs output"
    )
    assert "iPhone 14" in specs, (
        "Smartphone.get_specs failed: Expected 'iPhone 14' in specs output"
    )
    assert "A15 Bionic" in specs, (
        "Smartphone.get_specs failed: Expected 'A15 Bionic' in specs output"
    )
    assert "3.2GHz" in specs, (
        "Smartphone.get_specs failed: Expected '3.2GHz' in specs output"
    )
    assert "3279mAh" in specs, (
        "Smartphone.get_specs failed: Expected '3279mAh' in specs output"
    )
    assert "100% charged" in specs, (
        "Smartphone.get_specs failed: Expected '100% charged' in specs output"
    )


def test_smartphone_use_phone():
    """Test that using the phone reduces battery (1% per 10 minutes of use)."""
    phone = Smartphone("Apple", "iPhone 14", 3279, "A15 Bionic", 3.2)

    initial_charge = phone.battery.charge_level  # Should be 100%
    phone.use_phone(50)  # Use for 50 minutes = 5% reduction

    assert phone.battery.charge_level == initial_charge - 5, (
        "Smartphone.use_phone failed: Expected battery to be {}% after 50 minutes of use, got {}%".format(
            initial_charge - 5, phone.battery.charge_level
        )
    )


def test_smartphone_use_phone_boundary_zero():
    """Test that battery charge cannot go negative (boundary case: excessive use)."""
    phone = Smartphone("Apple", "iPhone 14", 3279, "A15 Bionic", 3.2)

    # Use phone excessively: 2000 minutes = 200% reduction (impossible)
    phone.use_phone(2000)

    # Battery should stop at 0%, not go negative
    assert phone.battery.charge_level >= 0, (
        "Smartphone.use_phone (boundary: zero) failed: Expected battery to not go negative, got {}%".format(
            phone.battery.charge_level
        )
    )
    assert phone.battery.charge_level == 0, (
        "Smartphone.use_phone (boundary: zero) failed: Expected battery to be exactly 0% after excessive use, got {}%".format(
            phone.battery.charge_level
        )
    )


def test_smartphone_use_phone_returns_charge():
    """Test that use_phone returns the new charge level after usage."""
    phone = Smartphone(
        "Google",           # brand
        "Pixel 7",          # model
        4355,               # battery_capacity
        "Google Tensor G2", # processor_model
        2.8                 # processor_speed
    )

    # Use for 30 minutes = 3% reduction (100% -> 97%)
    new_charge = phone.use_phone(30)

    assert new_charge == 97, (
        "Smartphone.use_phone (return value) failed: Expected return value to be 97, got {}".format(new_charge)
    )
    assert new_charge == phone.battery.charge_level, (
        "Smartphone.use_phone (return value) failed: Expected return value ({}) to match actual battery level ({})".format(
            new_charge, phone.battery.charge_level
        )
    )


def test_composition_component_parameters():
    """Test that Smartphone correctly passes parameters to its composed components."""
    phone = Smartphone(
        "Google",           # brand
        "Pixel 7",          # model
        4355,               # battery_capacity
        "Google Tensor G2", # processor_model
        2.8                 # processor_speed
    )

    # Verify components received correct parameters from smartphone constructor
    assert phone.battery.capacity == 4355, (
        "Composition (component parameters) failed: Expected battery capacity 4355, got {}".format(
            phone.battery.capacity
        )
    )
    assert phone.processor.model == "Google Tensor G2", (
        "Composition (component parameters) failed: Expected processor model 'Google Tensor G2', got '{}'".format(
            phone.processor.model
        )
    )
    assert phone.processor.speed == 2.8, (
        "Composition (component parameters) failed: Expected processor speed 2.8, got {}".format(
            phone.processor.speed
        )
    )


def test_smartphone_get_specs_all_info():
    """Test that get_specs contains all required phone specifications."""
    phone = Smartphone(
        "Samsung",            # brand
        "Galaxy S23",         # model
        3900,                 # battery_capacity
        "Snapdragon 8 Gen 2", # processor_model
        3.4                   # processor_speed
    )
    specs = phone.get_specs()

    # All these pieces of information should be in the specs string
    required_parts = [
        ("Samsung", "brand"),
        ("Galaxy S23", "model"),
        ("Snapdragon 8 Gen 2", "processor model"),
        ("3.4GHz", "processor speed"),
        ("3900mAh", "battery capacity"),
        ("100% charged", "charge level"),
    ]

    for part, description in required_parts:
        assert part in specs, (
            "Smartphone.get_specs (all info) failed: Missing {} '{}' in specs".format(description, part)
        )


def test_smartphone_get_battery_status_high():
    """Test battery status is 'High' when charge > 50%."""
    phone = Smartphone("Apple", "iPhone 14", 3279, "A15 Bionic", 3.2)

    # At 100% charge - should be High
    assert phone.get_battery_status() == "High", (
        "Smartphone.get_battery_status (High) failed: Expected 'High' at 100%, got '{}'".format(
            phone.get_battery_status()
        )
    )

    # At 51% (just above threshold) - should still be High
    phone.battery.charge_level = 51
    assert phone.get_battery_status() == "High", (
        "Smartphone.get_battery_status (High) failed: Expected 'High' at 51% (boundary: just above threshold), got '{}'".format(
            phone.get_battery_status()
        )
    )

    # At 75% - should be High
    phone.battery.charge_level = 75
    assert phone.get_battery_status() == "High", (
        "Smartphone.get_battery_status (High) failed: Expected 'High' at 75%, got '{}'".format(
            phone.get_battery_status()
        )
    )


def test_smartphone_get_battery_status_normal():
    """Test battery status is 'Normal' when 20% < charge <= 50%."""
    phone = Smartphone("Apple", "iPhone 14", 3279, "A15 Bionic", 3.2)

    # At 50% (upper boundary, > 20 but not > 50) - should be Normal
    phone.battery.charge_level = 50
    assert phone.get_battery_status() == "Normal", (
        "Smartphone.get_battery_status (Normal) failed: Expected 'Normal' at 50% (boundary: upper), got '{}'".format(
            phone.get_battery_status()
        )
    )

    # At 35% (middle of range) - should be Normal
    phone.battery.charge_level = 35
    assert phone.get_battery_status() == "Normal", (
        "Smartphone.get_battery_status (Normal) failed: Expected 'Normal' at 35%, got '{}'".format(
            phone.get_battery_status()
        )
    )

    # At 21% (just above low threshold) - should be Normal
    phone.battery.charge_level = 21
    assert phone.get_battery_status() == "Normal", (
        "Smartphone.get_battery_status (Normal) failed: Expected 'Normal' at 21% (boundary: just above Low), got '{}'".format(
            phone.get_battery_status()
        )
    )


def test_smartphone_get_battery_status_low():
    """Test battery status is 'Low' when charge <= 20%."""
    phone = Smartphone("Apple", "iPhone 14", 3279, "A15 Bionic", 3.2)

    # At 20% (boundary: not > 20, so Low) - should be Low
    phone.battery.charge_level = 20
    assert phone.get_battery_status() == "Low", (
        "Smartphone.get_battery_status (Low) failed: Expected 'Low' at 20% (boundary: upper), got '{}'".format(
            phone.get_battery_status()
        )
    )

    # At 19% - should be Low
    phone.battery.charge_level = 19
    assert phone.get_battery_status() == "Low", (
        "Smartphone.get_battery_status (Low) failed: Expected 'Low' at 19%, got '{}'".format(
            phone.get_battery_status()
        )
    )

    # At 10% - should be Low
    phone.battery.charge_level = 10
    assert phone.get_battery_status() == "Low", (
        "Smartphone.get_battery_status (Low) failed: Expected 'Low' at 10%, got '{}'".format(
            phone.get_battery_status()
        )
    )

    # At 0% (empty) - should be Low
    phone.battery.charge_level = 0
    assert phone.get_battery_status() == "Low", (
        "Smartphone.get_battery_status (Low) failed: Expected 'Low' at 0% (boundary: empty), got '{}'".format(
            phone.get_battery_status()
        )
    )

    # At 1% (critical) - should be Low
    phone.battery.charge_level = 1
    assert phone.get_battery_status() == "Low", (
        "Smartphone.get_battery_status (Low) failed: Expected 'Low' at 1% (critical), got '{}'".format(
            phone.get_battery_status()
        )
    )


def test_smartphone_get_battery_status_after_use():
    """Test that battery status changes correctly as phone is used."""
    phone = Smartphone("Apple", "iPhone 14", 3279, "A15 Bionic", 3.2)

    # Initial: High (100%)
    assert phone.get_battery_status() == "High", (
        "Smartphone.get_battery_status (after use) failed: Expected 'High' at initial 100%, got '{}'".format(
            phone.get_battery_status()
        )
    )

    # After 280 minutes (28% reduction): 72% - still High
    phone.use_phone(280)
    assert phone.get_battery_status() == "High", (
        "Smartphone.get_battery_status (after use) failed: Expected 'High' at 72% (after 280 min), got '{}'".format(
            phone.get_battery_status()
        )
    )

    # After 220 more minutes (22% reduction): 50% - now Normal (50 is not > 50)
    phone.use_phone(220)
    assert phone.get_battery_status() == "Normal", (
        "Smartphone.get_battery_status (after use) failed: Expected 'Normal' at 50% (after 500 min total), got '{}'".format(
            phone.get_battery_status()
        )
    )

    # After 290 more minutes (29% reduction): 21% - still Normal (21 > 20)
    phone.use_phone(290)
    assert phone.get_battery_status() == "Normal", (
        "Smartphone.get_battery_status (after use) failed: Expected 'Normal' at 21% (after 790 min total), got '{}'".format(
            phone.get_battery_status()
        )
    )

    # After 10 more minutes (1% reduction): 20% - now Low (20 is not > 20)
    phone.use_phone(10)
    assert phone.get_battery_status() == "Low", (
        "Smartphone.get_battery_status (after use) failed: Expected 'Low' at 20% (after 800 min total), got '{}'".format(
            phone.get_battery_status()
        )
    )


if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("Running Composition Tests")
    print("=" * 50 + "\n")

    test_battery_init()
    print("[PASSED] Battery.__init__")

    test_processor_init()
    print("[PASSED] Processor.__init__")

    test_smartphone_init()
    print("[PASSED] Smartphone.__init__")

    test_smartphone_init_owns_battery()
    print("[PASSED] Smartphone.__init__ (owns Battery)")

    test_smartphone_init_owns_processor()
    print("[PASSED] Smartphone.__init__ (owns Processor)")

    test_composition_independent_components()
    print("[PASSED] Composition: independent components")

    test_smartphone_get_specs()
    print("[PASSED] Smartphone.get_specs")

    test_smartphone_use_phone()
    print("[PASSED] Smartphone.use_phone")

    test_smartphone_use_phone_boundary_zero()
    print("[PASSED] Smartphone.use_phone (boundary: zero)")

    test_smartphone_use_phone_returns_charge()
    print("[PASSED] Smartphone.use_phone (return value)")

    test_composition_component_parameters()
    print("[PASSED] Composition: component parameters")

    test_smartphone_get_specs_all_info()
    print("[PASSED] Smartphone.get_specs (all info)")

    test_smartphone_get_battery_status_high()
    print("[PASSED] Smartphone.get_battery_status (High)")

    test_smartphone_get_battery_status_normal()
    print("[PASSED] Smartphone.get_battery_status (Normal)")

    test_smartphone_get_battery_status_low()
    print("[PASSED] Smartphone.get_battery_status (Low)")

    test_smartphone_get_battery_status_after_use()
    print("[PASSED] Smartphone.get_battery_status (after use)")

    print("\n" + "=" * 50)
    print("All composition tests passed!")
    print("=" * 50)
