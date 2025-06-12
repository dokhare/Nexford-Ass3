class PolicyProduct:

#create the init fuction which serves as the default function that creates new product when an object is intantiated
    def __init__(self, product_id, name, premium):
        self.product_id = product_id
        self.name = name
        self.premium = premium
        self.status = "Available"

# add two functions, update premium function and suspend product function
    def update_premium(self, new_premium):
        self.premium = new_premium
        print(f"💲 Product '{self.name}' premium updated to ${new_premium}")

    def suspend_product(self):
        self.status = "Suspended"
        print(f"🚫 Product '{self.name}' has been suspended.")
