import unittest
from datetime import date
import sys

# Print the module search path to help debug import issues
print("Module search path:", sys.path)

# Attempt to import all necessary classes, with error handling for debugging
try:
    from EBook import EBook
    from Discount import Discount
    from Customer import Customer, RegularCustomer, LoyalCustomer
    from ShoppingCart import ShoppingCart
    from Order import Order
    from Invoice import Invoice
    from Payment import Payment
except ImportError as e:
    print(f"ImportError: {e}")

class TestEBookStore(unittest.TestCase):

    def test_add_modify_ebook(self):
        # Create an eBook instance
        ebook = EBook("Sample Book", "Author A", date(2023, 1, 1), 29.99, "Fiction")

        # Test getTitle and getPrice
        self.assertEqual(ebook.getTitle(), "Sample Book")
        self.assertEqual(ebook.getPrice(), 29.99)

        # Modify title and price
        ebook.setTitle("New Title")
        ebook.setPrice(34.99)
        self.assertEqual(ebook.getTitle(), "New Title")
        self.assertEqual(ebook.getPrice(), 34.99)

        # Print eBook details
        print(ebook)

    def test_add_modify_customer(self):
        # Create a customer
        customer = Customer("Customer A", "customer@example.com", "C001")
        self.assertEqual(customer.getName(), "Customer A")

        # Modify customer name
        customer.setName("Customer B")
        self.assertEqual(customer.getName(), "Customer B")

        # Print customer details
        print(customer)

    def test_add_books_to_cart(self):
        # Create eBook and ShoppingCart instances
        ebook1 = EBook("Book One", "Author A", date(2023, 2, 1), 15.99, "Non-Fiction")
        ebook2 = EBook("Book Two", "Author B", date(2023, 3, 1), 20.99, "Science Fiction")
        cart = ShoppingCart("Cart001", "C001")

        # Add eBooks to the cart
        cart.addBook(ebook1)
        cart.addBook(ebook2)

        # Test total price
        self.assertEqual(cart.getTotal(), 36.98)

        # Print cart details
        print(cart)

    def test_apply_discount_for_loyal_customer(self):
        # Create a loyal customer and apply discount
        customer = LoyalCustomer("Loyal Customer", "loyal@example.com", "LC001")
        discount = customer.apply_discount()
        self.assertEqual(discount, 0.10)

        # Print discount for loyal customer
        print(f"Loyal Customer Discount: {discount * 100}%")

    def test_apply_bulk_discount(self):
        # Create a discount instance with bulk discount
        discount = Discount(0.15, 0.05, "D001", date(2023, 4, 1))

        # Test bulk discount
        self.assertEqual(discount.apply_bulk_discount(15), 0.15)  # Discount applied
        self.assertEqual(discount.apply_bulk_discount(5), 0)  # No discount

        # Print discount details
        print(discount)

    def test_generate_invoice_with_discount(self):
        # Create an eBook, customer, and order
        ebook = EBook("Book for Invoice", "Author C", date(2023, 5, 1), 50.00, "Mystery")
        customer = LoyalCustomer("Customer Invoice", "invoice@example.com", "CI001")
        order = Order("Order001", customer, 0.1, date(2023, 6, 1))

        # Create invoice with a loyalty discount and VAT
        discount = 0.10  # Loyalty discount
        vat = 0.2  # 20% VAT
        invoice = Invoice(order, discount, vat, "INV001")

        # Print invoice details
        print(invoice.generate_invoice())

    def test_payment_process(self):
        # Create a payment
        payment = Payment("Pay001", 100.0, date(2023, 7, 1), "Credit Card")

        # Test payment details
        self.assertEqual(payment._total, 100.0)

        # Print payment details
        print(payment)


# Run tests
if __name__ == "__main__":
    unittest.main(verbosity=2)
