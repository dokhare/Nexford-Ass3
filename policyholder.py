from datetime import datetime

class PolicyHolder:

#create the init fuction which serves as the default function that creates new policyholder when an object is intantiated
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.status = "Active"
        self.products = []
        self.payments = []

    def suspend(self):
        self.status = "Suspended"
        print(f"🔒 {self.name} has been suspended.")

    def reactivate(self):
        self.status = "Active"
        print(f"✅ {self.name} has been reactivated.")

    def register_product(self, product):
        if self.status == "Active":
            self.products.append(product)
            print(self.name+" registered for product "+product.name)
        else:
            print(f"⚠️ Cannot register product. {self.name} is not active.")

    def make_payment(self, payment):
        self.payments.append(payment)

    def get_details(self):
        print(f"\n--- Account Details for {self.name} ---")
        print(f"Email: {self.email}")
        print(f"Status: {self.status}")
        print("Products:")
        for p in self.products:
            print(f"  - {p.name} (${p.premium})")
        print("Payments:")
        for p in self.payments:
            print(f"  - ${p.amount} on {p.date.strftime('%Y-%m-%d')} | Status: {p.status}")
        print("-" * 40)
