from datetime import datetime

class Payment:

#create the init fuction which  serves as the default function that creates new payment when an object is intantiated
    def __init__(self, amount, due_date,status):
        self.amount = amount
        self.due_date = due_date
        self.date = datetime.now()
        self.status=status
        self.penalty = 0.0

# add two functions, apply penalty funciton and send reminder function
    def apply_penalty(self, rate=0.10):
        if self.status == "Late Payment":
            self.penalty = self.amount * rate
            self.amount += self.penalty
            print(f"⚠️ Late payment! Penalty of ${self.penalty:.2f} applied.")

    def send_reminder(self):
        print(f"📧 Reminder: Your payment of ${self.amount} is due by {self.due_date.strftime('%Y-%m-%d')}.")
