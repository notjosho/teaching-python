# Test file for Duck Typing Example
# Duck Typing: "If it walks like a duck and quacks like a duck, it's a duck"
# Objects are used based on behavior (methods), not type
from duck_typing_example import CreditCard, PayPal, Bitcoin, BankTransfer, process_all_payments


def test_creditcard_init():
    """Test that CreditCard requires verification (fraud protection)."""
    card = CreditCard()

    # Credit cards require verification for security
    assert card.requires_verification == True, (
        "CreditCard.__init__ failed: Expected requires_verification to be True, got {}".format(
            card.requires_verification
        )
    )


def test_paypal_init():
    """Test that PayPal requires verification (account-based)."""
    paypal = PayPal()

    # PayPal requires account verification
    assert paypal.requires_verification == True, (
        "PayPal.__init__ failed: Expected requires_verification to be True, got {}".format(
            paypal.requires_verification
        )
    )


def test_bitcoin_init():
    """Test that Bitcoin does NOT require verification (anonymous/decentralized)."""
    bitcoin = Bitcoin()

    # Bitcoin is decentralized and doesn't require traditional verification
    assert bitcoin.requires_verification == False, (
        "Bitcoin.__init__ failed: Expected requires_verification to be False, got {}".format(
            bitcoin.requires_verification
        )
    )


def test_banktransfer_init():
    """Test that BankTransfer requires verification (regulated financial system)."""
    bank = BankTransfer()

    # Bank transfers require verification through the banking system
    assert bank.requires_verification == True, (
        "BankTransfer.__init__ failed: Expected requires_verification to be True, got {}".format(
            bank.requires_verification
        )
    )


def test_creditcard_get_transaction_fee():
    """Test CreditCard fee: 2.5% of transaction amount."""
    card = CreditCard()

    # $100 * 2.5% = $2.50
    fee = card.get_transaction_fee(100)
    assert fee == 2.5, (
        "CreditCard.get_transaction_fee failed: Expected fee of $2.50 (2.5% of $100), got ${}".format(fee)
    )


def test_paypal_get_transaction_fee():
    """Test PayPal fee: 3% of amount + $0.30 fixed fee."""
    paypal = PayPal()

    # $100 * 3% + $0.30 = $3.30
    fee = paypal.get_transaction_fee(100)
    assert fee == 3.30, (
        "PayPal.get_transaction_fee failed: Expected fee of $3.30 (3% of $100 + $0.30), got ${}".format(fee)
    )


def test_bitcoin_get_transaction_fee():
    """Test Bitcoin fee: 1% of transaction amount."""
    bitcoin = Bitcoin()

    # $100 * 1% = $1.00
    fee = bitcoin.get_transaction_fee(100)
    assert fee == 1.0, (
        "Bitcoin.get_transaction_fee failed: Expected fee of $1.00 (1% of $100), got ${}".format(fee)
    )


def test_banktransfer_get_transaction_fee():
    """Test BankTransfer fee: flat $5.00 regardless of amount."""
    bank = BankTransfer()

    # Flat fee for $100
    fee_100 = bank.get_transaction_fee(100)
    assert fee_100 == 5.0, (
        "BankTransfer.get_transaction_fee failed: Expected flat fee of $5.00 for $100 transaction, got ${}".format(
            fee_100
        )
    )

    # Same flat fee for $1000 - doesn't change with amount
    fee_1000 = bank.get_transaction_fee(1000)
    assert fee_1000 == 5.0, (
        "BankTransfer.get_transaction_fee failed: Expected flat fee of $5.00 for $1000 transaction (same as $100), got ${}".format(
            fee_1000
        )
    )


def test_creditcard_process_payment():
    """Test CreditCard payment message includes amount and method name."""
    card = CreditCard()
    message = card.process_payment(100)

    # Message should mention the amount and payment type
    assert "100.00" in message, (
        "CreditCard.process_payment failed: Expected '100.00' in message, got '{}'".format(message)
    )
    assert "credit card" in message.lower(), (
        "CreditCard.process_payment failed: Expected 'credit card' in message (case insensitive), got '{}'".format(
            message
        )
    )


def test_paypal_process_payment():
    """Test PayPal payment message includes amount and method name."""
    paypal = PayPal()
    message = paypal.process_payment(100)

    assert "100.00" in message, (
        "PayPal.process_payment failed: Expected '100.00' in message, got '{}'".format(message)
    )
    assert "PayPal" in message, (
        "PayPal.process_payment failed: Expected 'PayPal' in message, got '{}'".format(message)
    )


def test_bitcoin_process_payment():
    """Test Bitcoin payment message includes amount and method name."""
    bitcoin = Bitcoin()
    message = bitcoin.process_payment(100)

    assert "100.00" in message, (
        "Bitcoin.process_payment failed: Expected '100.00' in message, got '{}'".format(message)
    )
    assert "bitcoin" in message.lower(), (
        "Bitcoin.process_payment failed: Expected 'bitcoin' in message (case insensitive), got '{}'".format(message)
    )


def test_banktransfer_process_payment():
    """Test BankTransfer payment message includes amount and method name."""
    bank = BankTransfer()
    message = bank.process_payment(100)

    assert "100.00" in message, (
        "BankTransfer.process_payment failed: Expected '100.00' in message, got '{}'".format(message)
    )
    assert "bank" in message.lower(), (
        "BankTransfer.process_payment failed: Expected 'bank' in message (case insensitive), got '{}'".format(message)
    )


def test_duck_typing_interface_contract():
    """Test that all payment types implement the same interface (duck typing contract)."""
    payment_methods = [CreditCard(), PayPal(), Bitcoin(), BankTransfer()]

    for method in payment_methods:
        class_name = type(method).__name__

        # All payment methods must have these methods/attributes
        assert hasattr(method, "process_payment"), (
            "{} (interface contract) failed: Missing required method 'process_payment'".format(class_name)
        )
        assert hasattr(method, "get_transaction_fee"), (
            "{} (interface contract) failed: Missing required method 'get_transaction_fee'".format(class_name)
        )
        assert hasattr(method, "requires_verification"), (
            "{} (interface contract) failed: Missing required attribute 'requires_verification'".format(class_name)
        )

        # Methods must be callable
        assert callable(getattr(method, "process_payment")), (
            "{} (interface contract) failed: 'process_payment' is not callable".format(class_name)
        )
        assert callable(getattr(method, "get_transaction_fee")), (
            "{} (interface contract) failed: 'get_transaction_fee' is not callable".format(class_name)
        )


def test_duck_typing_polymorphism():
    """Test that different payment types can be used interchangeably (polymorphism)."""
    payment_methods = [CreditCard(), PayPal(), Bitcoin(), BankTransfer()]

    # All payment methods work with the same code - no type checking needed
    for method in payment_methods:
        class_name = type(method).__name__

        # Can call same methods on all types
        message = method.process_payment(250)
        assert message is not None, (
            "{} (polymorphism) failed: process_payment(250) returned None".format(class_name)
        )
        assert isinstance(message, str), (
            "{} (polymorphism) failed: process_payment should return str, got {}".format(
                class_name, type(message).__name__
            )
        )

        fee = method.get_transaction_fee(250)
        assert fee is not None, (
            "{} (polymorphism) failed: get_transaction_fee(250) returned None".format(class_name)
        )
        assert isinstance(fee, (int, float)), (
            "{} (polymorphism) failed: get_transaction_fee should return int or float, got {}".format(
                class_name, type(fee).__name__
            )
        )


def test_fee_calculations_various_amounts():
    """Test fee calculations across multiple amounts for all payment types."""
    tolerance = 0.01  # Fee tolerance for floating point comparison

    test_cases = [
        # (PaymentMethod, amount, expected_fee, description)
        (CreditCard(), 100, 2.5, "CreditCard: 2.5% of $100"),
        (CreditCard(), 50, 1.25, "CreditCard: 2.5% of $50"),
        (PayPal(), 100, 3.30, "PayPal: 3% of $100 + $0.30"),
        (PayPal(), 200, 6.30, "PayPal: 3% of $200 + $0.30"),
        (Bitcoin(), 100, 1.0, "Bitcoin: 1% of $100"),
        (Bitcoin(), 1000, 10.0, "Bitcoin: 1% of $1000"),
        (BankTransfer(), 100, 5.0, "BankTransfer: flat $5 for $100"),
        (BankTransfer(), 10000, 5.0, "BankTransfer: flat $5 for $10000"),
    ]

    for payment_method, amount, expected_fee, description in test_cases:
        class_name = type(payment_method).__name__
        fee = payment_method.get_transaction_fee(amount)
        assert abs(fee - expected_fee) < tolerance, (
            "{}.get_transaction_fee failed: {} - Expected ${}, got ${}".format(
                class_name, description, expected_fee, fee
            )
        )


def test_duck_typing_no_type_checking():
    """Test that we can work with payments without isinstance checks (duck typing)."""
    payment_methods = [CreditCard(), PayPal(), Bitcoin(), BankTransfer()]

    # This function works without any type checking - pure duck typing
    for method in payment_methods:
        class_name = type(method).__name__

        # Just call the methods - "if it quacks like a duck, it IS a duck"
        result = method.process_payment(500)
        fee = method.get_transaction_fee(500)
        requires_v = method.requires_verification

        # We only care that the interface works, not what type it is
        assert isinstance(result, str), (
            "{} (no type checking) failed: process_payment should return str, got {}".format(
                class_name, type(result).__name__
            )
        )
        assert isinstance(fee, (int, float)), (
            "{} (no type checking) failed: get_transaction_fee should return number, got {}".format(
                class_name, type(fee).__name__
            )
        )
        assert isinstance(requires_v, bool), (
            "{} (no type checking) failed: requires_verification should be bool, got {}".format(
                class_name, type(requires_v).__name__
            )
        )


def test_verification_requirements():
    """Test that each payment type has correct verification requirement."""
    # Map of payment class to expected verification status
    verification_map = {
        CreditCard: (True, "fraud protection"),
        PayPal: (True, "account-based"),
        Bitcoin: (False, "decentralized"),
        BankTransfer: (True, "regulated"),
    }

    for payment_class, (expected_verification, reason) in verification_map.items():
        method = payment_class()
        class_name = payment_class.__name__
        assert method.requires_verification == expected_verification, (
            "{}.requires_verification failed: Expected {} ({} payment method), got {}".format(
                class_name, expected_verification, reason, method.requires_verification
            )
        )


def test_process_all_payments():
    """Test the process_all_payments function that demonstrates duck typing."""
    payment_methods = [CreditCard(), PayPal(), Bitcoin(), BankTransfer()]

    result = process_all_payments(
        payment_methods,
        [100, 250]  # amounts to process
    )

    # Should return a formatted string
    assert isinstance(result, str), (
        "process_all_payments failed: Expected return type str, got {}".format(type(result).__name__)
    )

    # Should contain the payment amounts
    assert "100.00" in result, (
        "process_all_payments failed: Expected '100.00' in result"
    )
    assert "250.00" in result, (
        "process_all_payments failed: Expected '250.00' in result"
    )

    # Should contain all payment method names
    assert "credit card" in result.lower(), (
        "process_all_payments failed: Expected 'credit card' in result (case insensitive)"
    )
    assert "paypal" in result.lower(), (
        "process_all_payments failed: Expected 'paypal' in result (case insensitive)"
    )
    assert "bitcoin" in result.lower(), (
        "process_all_payments failed: Expected 'bitcoin' in result (case insensitive)"
    )
    assert "bank transfer" in result.lower(), (
        "process_all_payments failed: Expected 'bank transfer' in result (case insensitive)"
    )

    # Should contain fee amounts (CreditCard: 2.5% of $100 and $250)
    assert "2.50" in result, (
        "process_all_payments failed: Expected '2.50' (CreditCard fee for $100) in result"
    )
    assert "6.25" in result, (
        "process_all_payments failed: Expected '6.25' (CreditCard fee for $250) in result"
    )

    # Should contain verification status for both verified and non-verified methods
    assert "True" in result, (
        "process_all_payments failed: Expected 'True' (verification status) in result"
    )
    assert "False" in result, (
        "process_all_payments failed: Expected 'False' (Bitcoin verification status) in result"
    )


if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("Running Duck Typing Tests")
    print("=" * 50 + "\n")

    test_creditcard_init()
    print("[PASSED] CreditCard.__init__")

    test_paypal_init()
    print("[PASSED] PayPal.__init__")

    test_bitcoin_init()
    print("[PASSED] Bitcoin.__init__")

    test_banktransfer_init()
    print("[PASSED] BankTransfer.__init__")

    test_creditcard_get_transaction_fee()
    print("[PASSED] CreditCard.get_transaction_fee")

    test_paypal_get_transaction_fee()
    print("[PASSED] PayPal.get_transaction_fee")

    test_bitcoin_get_transaction_fee()
    print("[PASSED] Bitcoin.get_transaction_fee")

    test_banktransfer_get_transaction_fee()
    print("[PASSED] BankTransfer.get_transaction_fee")

    test_creditcard_process_payment()
    print("[PASSED] CreditCard.process_payment")

    test_paypal_process_payment()
    print("[PASSED] PayPal.process_payment")

    test_bitcoin_process_payment()
    print("[PASSED] Bitcoin.process_payment")

    test_banktransfer_process_payment()
    print("[PASSED] BankTransfer.process_payment")

    test_duck_typing_interface_contract()
    print("[PASSED] Duck Typing: interface contract")

    test_duck_typing_polymorphism()
    print("[PASSED] Duck Typing: polymorphism")

    test_fee_calculations_various_amounts()
    print("[PASSED] Fee calculations: various amounts")

    test_duck_typing_no_type_checking()
    print("[PASSED] Duck Typing: no type checking needed")

    test_verification_requirements()
    print("[PASSED] Verification requirements")

    test_process_all_payments()
    print("[PASSED] process_all_payments")

    print("\n" + "=" * 50)
    print("All duck typing tests passed!")
    print("=" * 50)
