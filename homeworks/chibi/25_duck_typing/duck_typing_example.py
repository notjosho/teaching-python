class CreditCard:
    def __init__(self):
        self.requires_verification = True

    def process_payment(self, amount):
        return f"Processing ${amount:.2f} via credit card"

    def get_transaction_fee(self, amount):
        return amount * 0.025


class PayPal:
    def __init__(self):
        self.requires_verification = True

    def process_payment(self, amount):
        return f"Processing ${amount:.2f} via PayPal"

    def get_transaction_fee(self, amount):
        return amount * 0.03 + 0.30


class Bitcoin:
    def __init__(self):
        self.requires_verification = False

    def process_payment(self, amount):
        return f"Processing ${amount:.2f} via Bitcoin wallet"

    def get_transaction_fee(self, amount):
        return amount * 0.01


class BankTransfer:
    def __init__(self):
        self.requires_verification = True

    def process_payment(self, amount):
        return f"Processing ${amount:.2f} via bank transfer"

    def get_transaction_fee(self, amount):
        return 5.00


def process_all_payments(payment_methods, amounts):
    output = ""

    for amount in amounts:
        output += f"\n=== Processing Amount: ${amount:.2f} ===\n"

        for method in payment_methods:
            confirmation = method.process_payment(amount)
            fee = method.get_transaction_fee(amount)
            verification = str(method.requires_verification)  # <--- FIX

            output += (
                f"{confirmation}\n"
                f"Transaction fee: ${fee:.2f}\n"
                f"Requires verification: {verification}\n\n"
            )

    return output
