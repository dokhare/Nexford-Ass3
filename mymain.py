#import all the three modules and also import datetime
from datetime import datetime, timedelta
from policyholder import PolicyHolder
from product import PolicyProduct
from payment import Payment

# Create two products objects. 
p1 = PolicyProduct("P001", "Health Insurance", 1000)
p2 = PolicyProduct("P002", "Life Insurance", 800)

# Create two policyholders objects
joseph = PolicyHolder("Joseph Olamide", "josepholamide@gmail.com")
david = PolicyHolder("David Ifeanyi", "davidifeanyi@gmail.com")

# Register products
joseph.register_product(p1)
david.register_product(p2)

# create two payments objects for late payment, apply penalty and make payment for joseph and david
payment1 = Payment(1000, datetime.now() - timedelta(days=2),"Late Payment")
payment1.apply_penalty()
joseph.make_payment(payment1)

payment2 = Payment(800, datetime.now(),"Paid")
david.make_payment(payment2)

# Display details
joseph.get_details()
david.get_details()
