# 🛡️ Insurance Policy Management System

This project is a simple object-oriented **Insurance Policy Management System** written in Python. It allows policy managers to register and manage policyholders, assign insurance products, and track payments, including penalties and reminders.

---

## 📁 Project Structure

```

insurance\_system/
│
├── policyholder.py     # Defines the PolicyHolder class
├── product.py          # Defines the PolicyProduct class
├── payment.py          # Defines the Payment class
└── main.py             # Main script demonstrating usage

````

---

## ⚙️ Features

- Create, suspend, and reactivate policyholders
- Define and manage policy products (e.g. premium updates, suspension)
- Process payments, handle late penalties, and send reminders
- Display full policyholder account summaries

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.7+
- No external libraries required



### How to run

1. Open a terminal or command prompt.
2. Navigate to the project folder 
3. Run the script
   ```bash
   python main.py
   ```

---

## 📄 Usage Example

### Example Output

```
📄 Joseph  Olamide registered for product 'Health Insurance'
📄 David Ifeanyi registered for product 'Life Insurance'
⚠️ Late payment! Penalty of $100.00 applied.

--- Account Details for Joseph Olamide ---
Email: josepholamide@gmail.com
Status: Active
Products:
  - Health Insurance ($1000)
Payments:
  - $1100.0 on 2025-06-06 | Status: Late
----------------------------------------

--- Account Details for David Ifeanyi ---
Email: davidifeanyi@gmail.com
Status: Active
Products:
  - Life Insurance ($800)
Payments:
  - $800 on 2025-06-06 | Status: Paid
----------------------------------------
```

---

## 📚 File Descriptions

* `policyholder.py`: Manages policyholder registration, status, and links to payments/products.
* `product.py`: Manages insurance product creation, updates, and status control.
* `payment.py`: Manages payment processing, status detection, and penalties.
* `main.py`: Demonstrates full functionality using the defined classes.

---



## 📝 License

This project is open source and free to use for educational or internal business purposes.


## 💬 Contact

For improvements, feel free to open a pull request on my GitHub account or contact me directly - josephdokhare@gmail.com



